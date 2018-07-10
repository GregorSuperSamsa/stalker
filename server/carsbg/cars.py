# -*- coding: utf-8 -*-

import requests
from multiprocessing import Pool
import time
from bs4 import BeautifulSoup


class CarsAdd(object):
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


# https://www.cars.bg/?
# go=cars
# &search=1
# &advanced=0
# &fromhomeu=3
# &publishedTime=1
# &filterOrderBy=2
# &showPrice=0
# &autotype=1
# &stateId=1
# &filterOrderBy1=2
# &showPrice1=0
# &publishedTime1=1
# &brandId=8
# &modelId=0
# &yearFrom=
# &yearTo=&
# priceFrom=
# &priceTo=
# &currencyId=1
# &regionId=0
# &cityId=0
# &conditionId=0
# &photos=0
# &barter=0
# &dcredit=0
# &leasing=0
# &fuelId=0
# &gearId=0
# &usageId=0
# &steering_weel=0
# &categoryId=0
# &offerFrom1=0
# &offerFrom2=0
# &offerFrom3=0
# &offerFrom4=0
# &offersFor1=1
# &offersFor2=0
# &offersFor3=0&
# offersFor4=1
# &doorId=0
# &manual_price=0
# &man_priceFrom=0
# &man_priceTo=0

class CarsScraper(object):
    def __init__(self):
        self.url = ''
        self.query = ''



    @classmethod
    def scrap(self, query):
        result = []
        page = ''
        while '' == page:
            try:
                page = requests.get('https://bazar.bg/obiavi?q=' + query + '&sort=date')
            except:
                print("Connection refused by the server..")
                time.sleep(4)
                continue

        soup = BeautifulSoup(page.content, 'html.parser')

        array = soup.find_all('div', {'class': 'listItemContainer'})
        for html in array:

            tag_url = html.find('a', {'class': 'listItemLink'})
            if tag_url:
                # create BazarAdd object
                add = BazarAdd()

                # url
                add.url = tag_url['href']

                # thumbnail
                tag_thumbnail = html.find('img', {'class': 'cover'})
                if tag_thumbnail:
                    add.thumbnail = 'https:' + tag_thumbnail['src']
                else:
                    add.thumbnail = 'error'

                # title
                tag_title = html.find('span', {'class': 'title'})
                if tag_title:
                    add.headline = tag_title.get_text(strip=True)
                else:
                    add.headline = 'error'

                # price
                tag_price = html.find('span', {'class': 'price'})
                if tag_price:
                    add.price = tag_price.get_text(strip=True)
                else:
                    add.price = 'error'

                result.append(add)

        return result

    @classmethod
    def multiscrap(self, queries):
        p = Pool(len(queries))
        result = p.map(self.scrap, queries)
        p.terminate()
        p.join()
        return result


# def main():
#     scrapper = BazarScraper()
#     adds = scrapper.scrap('awo')
#     print('')
#     print('***************************************************')
#     for add in adds:
#         add_data = vars(add)
#         for single_data in add_data.items():
#             print('%s: %s' % single_data)
#             print('***************************************************')
#             print(add.headline)
#
#
# #
# #
# # # test purpose
# if __name__ == "__main__":
#     main()
