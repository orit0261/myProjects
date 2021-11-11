import logging
import re
from pathlib import Path
from typing import List, Dict

import requests
from bs4 import BeautifulSoup

log = logging.getLogger(__name__)


class AnimalScraper:
    animals_list = None

    async def get_animals_from_url(self) -> List[Dict]:
        WIKI_URL = 'https://en.wikipedia.org/wiki' + '/List_of_animal_names'
        ret_rows = list()
        req = requests.get(WIKI_URL)
        soup = BeautifulSoup(req.content, 'html.parser')

        tables = soup.find_all('table', {'class': 'wikitable sortable'})
        for table in tables:
            rows = table.findAll("tr")
            header_row = rows[0].find_all('th')

            for row in rows[1:]:  # jump over header
                cells = row.find_all('td')
                columns = dict()
                for x, y in zip(header_row, cells):#col header and it's value by row
                    if len(y.text) > 1:
                        columns[x.text.replace('\n', '')] = get_all_br(y)
                        if y.find('a', href=True) and 'href' in y.find('a', href=True).attrs:
                            columns[x.text.replace('\n', '') + '_href'] = y.find('a', href=True)['href']
                ret_rows.append(columns)
                self.animals_list = ret_rows
        return ret_rows

    async def get_animal_images(self, filter_func=lambda x: x, download_dir=None):
        """

        :param filter_func:
        :param download_dir: if None, download will not occur
        :return: list of files that have been downloaded
        """

        urls = ['https://en.wikipedia.org' + x['Animal_href'] for x in
                filter(filter_func, self.animals_list)
                if 'Animal_href' in x]

        return [await self.get_animal_image(url, download_dir) for url in urls]

    @staticmethod
    async def get_animal_image(url, download_dir=None):
        """

        :param url:
        :param download_dir: if None, download will not occur
        :return:
        """
        try:
            req = requests.get(url)
            soup = BeautifulSoup(req.content, 'html.parser')
            img = soup.find('img')

            image_url = 'https:' + img.attrs['src']

            r = requests.get(image_url, allow_redirects=True)
            if r.status_code == 200:
                filename = img.attrs["alt"]
                p = Path(download_dir, filename)
                if filename!='':
                  with open(p, 'wb') as fp:
                    fp.write(r.content)
                return p

        except Exception as e:
            log.exception(f'url: {url} failed to load/parse', e)
        finally:
            pass


#### util functions


def clean_text(text):
    ret = re.sub('[^a-zA-Z, ]+', ',', text).lower()

    return ret


def get_all_br(item):
    lst = item.find_all('br')#<br> tag inserts a single line break
    if len(lst) > 0:
        ret = [clean_text(x.text) for x in lst]
    elif ',' in item.text:
        ret = [clean_text(x) for x in item.text.split(',') if len(x) > 1]
    elif ' or ' in item.text:
        ret = [clean_text(x) for x in item.text.split(' or ') if len(x) > 1]
    else:
        ret = [clean_text(item.text)]
    return ret
