from collections import defaultdict

import asyncio
import logging

from wikipedia.AnimalScraper import AnimalScraper
from wikipedia import htmlcon

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] [%(levelname)s] [%(module)s.%(funcName)s] %(message)s',
                    datefmt="%H:%M:%S",
                    handlers=[logging.FileHandler("animals.log", mode='w'), logging.StreamHandler()])

log = logging.getLogger(__name__)


async def main():

    connector = AnimalScraper()
    animal_rows = await connector.get_animals_from_url()

    images = await connector.get_animal_images(lambda x: x, 'images/')
    print(images)

    grouped_by_key = await group_by(animal_rows, key='Collateral adjective')

    await print_all_animals_by_key(grouped_by_key)
    print(dict(grouped_by_key))
    htmlcon.dictionaryToHTML3(dict(grouped_by_key))


async def print_all_animals_by_key(grouped_by_key):
    for a, adj in enumerate(sorted(grouped_by_key.keys())):

        log.info(f'[{a} {adj}]')

        for i, anim in enumerate(grouped_by_key[adj], 1):
            log.info(f'{i}, {anim}')
            #await htmlcon.dictionaryToHTML(anim)
            # Html_file= open("animal.html","w")
            # Html_file.write(str(html_f))
            # Html_file.close()

async def group_by(animal_rows, key):
    d2 = defaultdict(list)
    # d2 = Counter()
    for animal in animal_rows:

        if key in animal.keys():
            for item in animal[key]:
                d2[item].append(animal)
    #               d2[item] +=1
    return d2


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
