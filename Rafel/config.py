# global variables for db connection
#db = create_engine('postgresql+psycopg2://postgres:orit0261@localhost:5432/dev')
POSTGRES_USER='postgres'
POSTGRES_PW='orit0261'
POSTGRES_URL = 'localhost'
POSTGRES_PORT = '5432'
POSTGRES_DB = 'dev'
DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
