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
        ls = connect.engine.execute(s).fetchall()
        return True
    except Exception as e:
        print(e, "error")
        return False
    finally:
        connect.engine.dispose()


if __name__ == '__main__':
    #print(gf.generate_random_string())
    select_from_table('customers')
    create_ads()
    print(gf.qsort(['ab', 'ba', 'rtg', 'aba', 'aaa', 'abc', 'bdd']))
