import pyodbc
print(pyodbc.drivers())
#conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=./SQLEXPRESS;'

 #                     'DATABASE=Employee_db;Trusted_Connection = yes;')

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=ORIT-DELL\SQLEXPRESS;'
                      'Database=Employee_db;'
                      'Trusted_Connection=yes;')
print(conn)
cur = conn.cursor()
cur.execute('select * from dbo.emp_details;')
for i in cur:
    print(i)