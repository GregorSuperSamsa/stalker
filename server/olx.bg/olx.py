# -*- coding: utf-8 -*-

import multiprocessing
import requests
import time
from bs4 import BeautifulSoup


class OlxAdd(object):
    def __init__(self):
        self.headline = ''
        self.text = ''
        self.price = ''
        self.location = ''
        self.date = ''
        self.user = ''
        self.phone = ''
        self.url = ''
        self.thumbnail = ''
        self.images = []


class OlxScraper(object):
    def __init__(self):
        self.url = ''
        self.query = ''

    def set_query(self, query):
        self.query = query
        self.url = 'https://www.olx.bg/ads/q-' + query + '/?search%5Bdescription%5D=1'

    @property
    def scrap(self):
        result = []
        page = ''
        while page == '':
            try:
                page = requests.get(self.url)
            except:
                print("Connection refused by the server..")
                print("Let me sleep for 5 seconds")
                print("ZZzzzz...")
                time.sleep(5)
                print("Was a nice sleep, now let me continue...")
                continue

        soup = BeautifulSoup(page.content, 'html.parser')

        array = soup.find_all('td', {'class': 'offer'})
        for html in array:
            tag_headline = html.find('strong')
            # found possible add in html
            if tag_headline:
                headline = tag_headline.text.strip()
                if headline:
                    # create OlxAdd object
                    add = OlxAdd()

                    # headline
                    add.headline = headline

                    # url
                    tag_url = html.find('a', {'class': 'marginright5 link linkWithHash detailsLink'})
                    if tag_url:
                        add.url = tag_url['href']
                    else:
                        add.url = 'error'

                    # thumbnail
                    tag_thumbnail = html.find('img', {'class': 'fleft'})
                    if tag_thumbnail:
                        add.thumbnail = tag_thumbnail['src']
                    else:
                        add.thumbnail = 'error'


                    # location
                    tag_location = html.find('p', {'class': 'color-9 lheight16 marginbott5'}).find('span')
                    if tag_location:
                        add.location = tag_location.text.strip()
                    else:
                        add.location = 'error'

                    # date
                    tag_date = html.find('p', {'class': 'color-9 lheight16 marginbott5 x-normal'})
                    if tag_date:
                        add.date = tag_date.text.strip()
                    else:
                        add.date = 'error'

                    # price
                    tag_price = html.find('p', {'class': 'price'})
                    if tag_price:
                        add.price = tag_price.strong.text.strip()
                    else:
                        add.price = 'error'

                    result.append(add)

        return result


def main():
    scrapper = OlxScraper()
    scrapper.set_query('recaro')
    adds = scrapper.scrap
    print('')
    print('***************************************************')
    for add in adds:
        add_data = vars(add)
        for single_data in add_data.items():
            print('%s: %s' % single_data)
        print('***************************************************')


# test purpose
if __name__ == "__main__":
    main()