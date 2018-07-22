# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from bs4 import SoupStrainer


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
#
#
def main():
    # cache
    # no images
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    prefs = {"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096}
    chrome_options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.implicitly_wait(300)
    driver.get('https://www.cars.bg/?go=home')

    driver.find_element_by_link_text('Разширено търсене').click()

    value = 'Мотори'
    select_element = Select(driver.find_element_by_name('section'))
    select_element.select_by_visible_text(value)

    value = 'Avo'
    select_element = Select(driver.find_element_by_name('brand_motoId'))
    select_element.select_by_visible_text(value)

    driver.find_element_by_name('yearFrom').send_keys('1900')
    driver.find_element_by_name('yearTo').send_keys('2000')

    driver.find_element_by_name('offersFor3').click()

    driver.find_element_by_link_text('Търсене').click()

    driver.execute_script('ConsentAnswear("no")')
    time.sleep(3)

    html = driver.page_source

    strainer = SoupStrainer('table', {'class': 'tableListResults'})

    soup = BeautifulSoup(html, 'html.parser', parse_only=strainer)

    adds = soup.find_all('tr', {'class': ['odd ', 'even ', 'odd last', 'even last']})
    for add in adds:
        obj = CarsAdd()
        #
        headline = add.find('span', {'class': 'ver15black'})
        if headline:
            obj.headline = headline.text.strip()
        else:
            obj.headline = 'error'
        #
        url = add.find('a')
        if url:
            obj.url = url['href']
            print(url)
        else:
            obj.url = 'error'

        print(obj.headline)
        print(obj.url)
        print('')


    driver.quit()

# test purpose
if __name__ == "__main__":
    main()


#
#
# # https://www.cars.bg/?
# # go=cars
# # &search=1
# # &advanced=0
# # &fromhomeu=3
# # &publishedTime=1
# # &filterOrderBy=2
# # &showPrice=0
# # &autotype=1
# # &stateId=1
# # &filterOrderBy1=2
# # &showPrice1=0
# # &publishedTime1=1
# # &brandId=8
# # &modelId=0
# # &yearFrom=
# # &yearTo=&
# # priceFrom=
# # &priceTo=
# # &currencyId=1
# # &regionId=0
# # &cityId=0
# # &conditionId=0
# # &photos=0
# # &barter=0
# # &dcredit=0
# # &leasing=0
# # &fuelId=0
# # &gearId=0
# # &usageId=0
# # &steering_weel=0
# # &categoryId=0
# # &offerFrom1=0
# # &offerFrom2=0
# # &offerFrom3=0
# # &offerFrom4=0
# # &offersFor1=1
# # &offersFor2=0
# # &offersFor3=0&
# # offersFor4=1
# # &doorId=0
# # &manual_price=0
# # &man_priceFrom=0
# # &man_priceTo=0
#
# class CarsScraper(object):
#     def __init__(self):
#         self.url = ''
#         self.query = ''
#
#
#
#     @classmethod
#     def scrap(self, query):
#         result = []
#         page = ''
#         while '' == page:
#             try:
#                 page = requests.get('https://bazar.bg/obiavi?q=' + query + '&sort=date')
#             except:
#                 print("Connection refused by the server..")
#                 time.sleep(4)
#                 continue
#
#         soup = BeautifulSoup(page.content, 'html.parser')
#
#         array = soup.find_all('div', {'class': 'listItemContainer'})
#         for html in array:
#
#             tag_url = html.find('a', {'class': 'listItemLink'})
#             if tag_url:
#                 # create BazarAdd object
#                 add = BazarAdd()
#
#                 # url
#                 add.url = tag_url['href']
#
#                 # thumbnail
#                 tag_thumbnail = html.find('img', {'class': 'cover'})
#                 if tag_thumbnail:
#                     add.thumbnail = 'https:' + tag_thumbnail['src']
#                 else:
#                     add.thumbnail = 'error'
#
#                 # title
#                 tag_title = html.find('span', {'class': 'title'})
#                 if tag_title:
#                     add.headline = tag_title.get_text(strip=True)
#                 else:
#                     add.headline = 'error'
#
#                 # price
#                 tag_price = html.find('span', {'class': 'price'})
#                 if tag_price:
#                     add.price = tag_price.get_text(strip=True)
#                 else:
#                     add.price = 'error'
#
#                 result.append(add)
#
#         return result
#
#     @classmethod
#     def multiscrap(self, queries):
#         p = Pool(len(queries))
#         result = p.map(self.scrap, queries)
#         p.terminate()
#         p.join()
#         return result






