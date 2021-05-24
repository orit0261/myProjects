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

    def create_results_Table(self):
        self.table_name = 'results'
        try:
            query = 'DROP TABLE if exists ' + self.table_name
            self.engine.connect().execute(query)
            query =("""create table {}( {} serial, {} text, {} text, {} text, {} text,{} text,{} text)""").format(self.table_name,
                                                                             '"{}"'.format("Index"),
                                                                              '"{}"'.format("Sorting - step1"),
                                                                              '"{}"'.format("Sorting - step1_Process_time"),
                                                                              '"{}"'.format("Sorting - step2"),
                                                                              '"{}"'.format("Sorting - step2_Process_time"),
                                                                              '"{}"'.format("Sorting - step3"),
                                                                              '"{}"'.format("Sorting - step3_Process_time"))

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

