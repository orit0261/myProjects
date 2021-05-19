import random
import time

import psycopg2

import general_functions as gf
import sqlconnect
from Rafel import config


class create_psycopg:
    def __init__(self):
        self.__con = psycopg2.connect(database=config.POSTGRES_DB, user=config.POSTGRES_USER,
                                      password=config.POSTGRES_PW)
        self.__cur = self.__con.cursor()

    def select_from_table_phase_1(self, tbl, get_field, tbl_res):
        t1 = time.time()
        try:
            sql = """SELECT {} FROM {}""".format('"{}"'.format(get_field), tbl)
            self.__cur.execute(sql)
            ls = list(self.__cur.fetchall())
            ls_sort = sorted(ls)
            values = tuple(ls_sort)
            # insert tuples to results table
            self.__cur.executemany("insert into " + tbl_res + " values (%s);", values)
            self.__con.commit()

            t2 = time.time()
            print(f'the time for phase-1 : {t2 - t1:.2f} seconds')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
        finally:
            if self.__con:
                self.__con.close()

    def select_from_table_phase_2(self, tbl, get_field, ioffset, irows=2000):
        t1 = time.time()
        try:
            sql = """SELECT {} FROM {} OFFSET {} FETCH FIRST {} ROW ONLY""" \
                .format('"{}"'.format(get_field), tbl, ioffset, irows)
            self.__cur.execute(sql)
            ls = list(self.__cur.fetchall())
            # ls_sort = sorted(ls)
            # values = tuple(ls_sort)
            # insert tuples to results table
            # self.__cur.executemany("insert into " + tbl_res + " values (%s);", values)
            # self.__con.commit()

            t2 = time.time()
            print(f'the time for phase-1 : {t2 - t1:.2f} seconds')
        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
        finally:
            if self.__con:
                self.__con.close()


if __name__ == '__main__':
    js = gf.get_dic()
    connect = sqlconnect.connectSQL(**js)

    # connect.create_ads_Table('ads_tbl')

    # for i in range(1,20000):
    # connect.insert_ads_Table(random.randint(0,200000), gf.generate_random_string())

    # connect.create_results_Table()

    obj_psy = create_psycopg()
    # obj_psy.select_from_table_phase_1('ads_tbl','Name','results')
    obj_psy.select_from_table_phase_2('results', 'Sorting - step1', 0)

    print(gf.qsort(['ab', 'ba', 'rtg', 'aba', 'aaa', 'abc', 'bdd']))
