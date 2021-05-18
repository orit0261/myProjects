import random
import time

import psycopg2

import general_functions as gf
import sqlconnect
from Rafel import config


def create_ads():
    js = gf.get_dic()
    connect = sqlconnect.connectSQL(**js)
    try:
        connect.create_ads_Table('ads_tbl')
        return True
    except Exception as e:
        print(e, "error creating ads table")
        return False
    finally:
        connect.engine.dispose()


def select_from_table(tbl,get_field,tbl_res,field_name):
    t1 = time.time()
    con = psycopg2.connect(database=config.POSTGRES_DB, user=config.POSTGRES_USER,
                           password=config.POSTGRES_PW)

    try:
        cur = con.cursor()
        sql = """SELECT {} FROM {}""".format('"{}"'.format(get_field),tbl)
        cur.execute(sql)
        ls = list(cur.fetchall())
        ls_sort = sorted(ls)
        values = tuple(ls_sort)
        cur.executemany("insert into results values (%s);", values)
        con.commit()

        t2 = time.time()
        print(t2-t1)
        return True
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
        return False
    finally:
        if con:
            con.close()



if __name__ == '__main__':
    js = gf.get_dic()
    connect = sqlconnect.connectSQL(**js)
    connect.create_results_Table('RESULTS', "Sorting-step1")

    #connect.create_ads_Table('ads_tbl')
   # for i in range(1,20000):
     #connect.insert_ads_Table(random.randint(0,200000), gf.generate_random_string())
    select_from_table('ads_tbl','Name','results','Sorting-step1')
    print(gf.qsort(['ab', 'ba', 'rtg', 'aba', 'aaa', 'abc', 'bdd']))
