from datetime import datetime
import re
import sqlalchemy as sq


class connectSQL:

    def __init__(self, username, host, port, database, password):
        # create connection to Postgres
        '''
        :param username: DB username
        :param port:  DB port
        :param database: DB name
        :param password:  DB global password
        :param host: DB host ID
        :return: connection to the DB
        '''

        self.username = username
        self.host = host
        self.port = port
        self.database = database
        self.password = password
        engine = sq.create_engine('postgresql://' + self.username + ':' + self.password + '@' + self.host + ':' \
                                  + self.port + '/' + self.database)
        self.engine = engine

    def createTable(self, df, table_name):
        # create table
        '''
        :param dir: table path
        :param table_name: DB wanted table name
        '''
        self.table_name = table_name

        query = 'DROP TABLE if exists public.' + self.table_name
        self.engine.connect().execute(query)

        df.columns = map(lambda x: re.sub(r"[^\w\s]", "", x), df.columns)
        print("Starting to work on the table.. " + str(datetime.now()))
        df.to_sql(self.table_name, con=self.engine.connect(), schema="dev", index=False)
        print('Table {} has been added successfully'.format(self.table_name))

    def create_results_Table(self,table_name,field_name):
        self.table_name = table_name
        try:
            query = 'DROP TABLE if exists ' + self.table_name
            self.engine.connect().execute(query)
            query =("""create table {}( {} text)""").format(self.table_name,'"{}"'.format(field_name))

            self.engine.connect().execute(query)
            print('Table {} has been added successfully'.format(self.table_name))

        except Exception as e:
            print(e, "error in creating table")
        finally:
            self.engine.dispose()


    def create_ads_Table(self,table_name):
        # create table
        '''
        :param dir: table path
        :param table_name: DB wanted table name
        '''
        self.table_name = table_name
        try:
            query = 'DROP TABLE if exists ' + self.table_name
            self.engine.connect().execute(query)

            query = (
                """create table ads_tbl(
                         "Index" serial PRIMARY KEY, 
                         "Id" text NOT NULL,
                         "Name" text
                         )"""
            )
            self.engine.connect().execute(query)
            print('Table {} has been added successfully'.format(self.table_name))

        except Exception as e:
            print(e, "error in creating ads table")
        finally:
            self.engine.dispose()



    def insert_ads_Table(self,f_id,f_name=''):
        try:
            query = """INSERT INTO ads_tbl ("Id", "Name")
                         VALUES(%s, %s)"""
            self.engine.connect().execute(query,(f_id,f_name,))
            print('record has been added successfully to ads table')

        except Exception as e:
            print(e, "error in insert ads table")
        finally:
            self.engine.dispose()


