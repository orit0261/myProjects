from datetime import datetime
list1=["30-4-1994","1994-30-04","30/04/1994","30-apr-1994","30/apr/1994","1994-30-apr"]
for i in list1:
    for fmt in ('%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y',
                  '%Y-%d-%m', '%Y-%d-%b', '%d-%b-%Y', '%d/%b/%Y'):
        try:
           example_time =  datetime.strptime(i, fmt).date()
           final_output =  datetime.strftime(example_time, "%d-%m-%Y")
           print(final_output)
        except ValueError:
           continue


import dateutil.parser as dparser
a = ["12-8-2017", "27/08/17", "8/9/2017", "10/9/2017", "15/09/17"]
a = ["2010/03/30", "15/12/2016", "11-15-2012", "20130720","30-30-2020"]
ls=list()
correctDate = None
try:
    for i in a:
        ls.append(dparser.parse(i,fuzzy=True).date().strftime('%Y%m%d'))
        print(dparser.parse(i,fuzzy=True).date().strftime('%Y%m%d'))
except ValueError:
    correctDate = False
print(ls)
