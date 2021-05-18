import random

import general_functions as gf
import sqlconnect


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


def select_from_table(tbl):
    js = gf.get_dic()
    connect = sqlconnect.connectSQL(**js)
    try:
        s = f"select * from {tbl}"
        ls = list(connect.engine.execute(s).fetchall())
        ls_sort = sorted(ls, key=lambda x: x[2])

        return True
    except Exception as e:
        print(e, "error")
        return False
    finally:
        connect.engine.dispose()


if __name__ == '__main__':
    js = gf.get_dic()
    connect = sqlconnect.connectSQL(**js)
    connect.create_ads_Table('ads_tbl')
    for i in range(1,20000):
        connect.insert_ads_Table(random.randint(0,200000), gf.generate_random_string())

    print(gf.qsort(['ab', 'ba', 'rtg', 'aba', 'aaa', 'abc', 'bdd']))
