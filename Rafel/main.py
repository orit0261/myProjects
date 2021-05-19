from time import perf_counter
import psycopg2

import general_functions as gf
import sqlconnect
from Rafel import config


class create_psycopg:
    def __init__(self):
        self.__con = psycopg2.connect(database=config.POSTGRES_DB, user=config.POSTGRES_USER,
                                      password=config.POSTGRES_PW)
        self.__cur = self.__con.cursor()
        self.__global_lst = []

    def __del__(self):
        if self.__con:
            self.__con.close()

    def __update_times(self, tbl_res, target_field, ttime, rec_num):
        target_field = '"{}"'.format(target_field)
        index_field = '"{}"'.format('Index')

        self.__cur.execute(
            "UPDATE {} SET {} = {} WHERE {}={}".format(tbl_res, target_field, str(ttime), index_field, rec_num))
        try:
            self.__con.commit()
        except psycopg2.DatabaseError as e:
            print(f'Error in updating times {e}')

    def exec_phase_1(self, tbl, get_field, tbl_res):
        t1 = perf_counter()  # time.time()
        try:
            sql = """SELECT {} FROM {}""".format('"{}"'.format(get_field), tbl)
            self.__cur.execute(sql)
            ls = list(self.__cur.fetchall())
            ls_sort = sorted(ls)
            values = tuple(ls_sort)
            # insert tuples to results table
            target_field = '("{}")'.format('Sorting - step1')
            self.__cur.executemany("INSERT INTO " + tbl_res + target_field + " VALUES (%s);", values)
            self.__con.commit()

            t2 = perf_counter()  # time.time()

            self.__update_times('results', 'Sorting - step1_Process_time', t1, 1)
            self.__update_times('results', 'Sorting - step1_Process_time', t2, 20000)

            print(f'the time for phase-1 : {t2 - t1:.2f} seconds')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')

    def exec_phase_2(self, tbl, get_field, irows=2000, prlel=False):
        if prlel:
            nfield = 'Sorting - step3'
            num = 3
            tfield = 'Sorting - step3_Process_time'
        else:
            nfield = 'Sorting - step2'
            num = 2
            tfield = 'Sorting - step2_Process_time'
        print(f'\nStart Phase - {num}')
        t1 = perf_counter()  # time.time()
        print('t1=', t1)
        self.__update_times('results', tfield, t1, 1)

        [self.select_from_table_phase_2(tbl, get_field, i, parallel=prlel)
         for i in range(0, 200000, irows)]

        if prlel:
            gf.sort_parallel(self.__global_lst, 4)

        t2 = perf_counter()
        print('t2=', t2)
        self.__update_times('results', tfield, t2, 20000)
        print(f"\nPhase - {num} takes {t2 - t1:0.4f} seconds")
        print(f'\nFinished Phase - {num}')

        target_field = '"{}"'.format(nfield)
        index_field = '"{}"'.format('Index')
        for i, v in enumerate(self.__global_lst):
            self.__cur.execute(
                "UPDATE results SET {}={} WHERE ({}={})".format(target_field, "'{}'".format(v), index_field, i + 1))
            self.__con.commit()


    def select_from_table_phase_2(self, tbl, get_field, ioffset, irows=2000, parallel=False):
        try:
            sql = """SELECT {} FROM {} ORDER BY {} OFFSET {} FETCH FIRST {} ROW ONLY""" \
                .format('"{}"'.format(get_field), tbl, '"{}"'.format(get_field), ioffset, irows)
            self.__cur.execute(sql)
            ls = list(self.__cur.fetchall())
            # convert tuple to list
            ls_sort = [item for t in ls for item in t]
            # ls_sort = sorted(ls_sort)
            # merge ls_sort with global list and sort it
            self.__global_lst = self.__global_lst + ls_sort
            if not parallel:
                self.__global_lst = gf.mergeSort(self.__global_lst, 0, len(self.__global_lst) - 1)
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')


if __name__ == '__main__':
    js = gf.get_dic()
    connect = sqlconnect.connectSQL(**js)

    connect.create_ads_Table('ads_tbl')

    for i in range(1,20001):
      connect.insert_ads_Table(random.randint(0,200000), gf.generate_random_string())

    connect.create_results_Table()

    obj_psy = create_psycopg()

    obj_psy.exec_phase_1('ads_tbl', 'Name', 'results')
    obj_psy.exec_phase_2('ads_tbl', 'Name', irows=2000)
    obj_psy.exec_phase_2('ads_tbl', 'Name', irows=2000, prlel=True)
