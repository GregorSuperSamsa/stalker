# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from collections import  namedtuple


Search = namedtuple('Search', 'section, brand')
Search = Search('cars', ['lada', 'bmw'])



# class Search:
#     class Cars:
#         section = "cars"
#         class Brand:
#             lada = "lada"
#     class Motorcycles:
#         class Brand:
#             awo = "avo"

    # class Buses:
    #     buses       = "busove"
    # motorcycles = "moto"
    # campers     = "caravan"
    # trucks      = "truck"
    # boats       = "boat"
    # bagers      = "bager"
    # agro        = "agro"
    # trailer     = "trailer"
    # parts       = "part"
    # tires       = "tire"

#class Brand:
#    lada = "lada"
        # buses = "busove"
        # motorcycles = "moto"
        # caravan = "caravan"
        # trucks = "truck"
        # boats = "boat"
        # bagers = "bager"
        # agro = "agro"
        # trailer = "trailer"
        # parts = "part"
        # tires = "tire"


class CarsScrapper(Search):
    #Section = Enum('Section', 'cars busove moto caravan truck boat bager agro trailer part tire')


    def __init__(self):
        #self.section = self.Section.cars.name
        self.brand = ""
        self.model = ""
        self.year_from = ""
        self.year_to = ""
        self.pages = -1

    def setup(self):
        pass
        #print(self.section)

    def setSection(self, section):
        self.section = section
        print(self.section)

    def setBrand(self, brand):
        self.brand = brand
        print(self.brand)





class CarsAdd(object):
    def __init__(self):
        self.title = ''
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


    scrapper = CarsScrapper()

    scrapper.setSection(Search.Cars.Brand.lada)
    scrapper.setBrand(Brand.lada)
    scrapper.setup()

    #cached
    #no images
    chrome_options = webdriver.ChromeOptions()
    #headless
    chrome_options.add_argument('headless')
    prefs = {"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096}
    chrome_options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.implicitly_wait(300)
    driver.get('https://www.cars.bg/?go=home')

    driver.find_element_by_link_text('Разширено търсене').click()

    value = 'Мотори'
    select_element = Select(driver.find_element_by_name('section'))
    select_element.select_by_value('moto')

    value = 'Avo'
    select_element = Select(driver.find_element_by_name('brand_motoId'))
    select_element.select_by_visible_text(value)

    driver.find_element_by_name('yearFrom').send_keys('1900')
    driver.find_element_by_name('yearTo').send_keys('2000')



    #for parts
    driver.find_element_by_name('offersFor3').click()
    #broken/hit
    driver.find_element_by_name('offersFor2').click()



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
        title = add.find('span', {'class': 'ver15black'})
        if title:
            obj.title = title.text.strip()
        else:
            obj.headline = 'error'
        #
        url = add.find('a')
        if url:
            obj.url = url['href']
            print(url)
        else:
            obj.url = 'error'

        print(obj.title)
        print(obj.url)
        print('')


    driver.quit()


#test purpose
if __name__ == "__main__":
    main()
