import requests
import pandas as pd
from sqlalchemy import create_engine

def read_apis(url_address):
   return requests.get(url_address).json()


def read_html_2():
    deriv=requests.get('https://data.gov.il/api/3/action/datastore_search')
    df2 = pd.read_html(deriv.find_element_by_id("history_table").get_attribute('outerHTML'))[0]


if __name__=='__main__':
    engine = create_engine('mssql+pymssql://Orit:orit0261@localhost:5432/ORIT')

    df1=pd.read_html('https://www.geonames.org/countries/')
    df1 = df1[1]
    #read_html_2()
    #df2= read_apis('https://data.gov.il/dataset/flydata/resource/e83f763b-b7d7-479e-b172-ae981ddc6de5')
    df2= pd.read_html('https://data.gov.il/api/3/action/datastore_search')
    df3=pd.read_json('http://universities.hipolabs.com/search?name=middle')

    df1.to_sql('countries', con=engine, if_exists='replace')
    df2.to_sql('flights', con=engine, if_exists='replace')
    df3.to_sql('universites', con=engine, if_exists='replace')


