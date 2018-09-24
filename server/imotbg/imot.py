# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from enum import Enum


class ImotScrapper(object):
    def __init__(self):
        self.Section = Enum('Section', 'cars busove moto caravan truck boat bager agro trailer part tire')
        self.section = self.Section.cars.name
        self.brand = ""
        self.model = ""
        self.year_from = ""
        self.year_to = ""
        self.pages = -1

    def setup(self):
        pass
        #print(self.section)





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
    scrapper = ImotScrapper()
    scrapper.setup()

    #cached
    #no images
    chrome_options = webdriver.ChromeOptions()
    #headless
    #chrome_options.add_argument('headless')
    prefs = {"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096}
    chrome_options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.implicitly_wait(300)
    driver.get('https://www.imot.bg/')

    # Sales
    driver.find_element_by_link_text('Продажби').click()

    # Area
    select_element = Select(driver.find_element_by_name('f38'))
    select_element.select_by_value('област Варна')

    # House
    driver.find_element_by_id('vi10').click()

    # Specific areas
    # - Kichevo
    select_element = Select(driver.find_element_by_name('ri'))
    select_element.select_by_value('с. Кичево')
    driver.execute_script('javascript:toright()')

    select_element = Select(driver.find_element_by_name('f41'))
    select_element.select_by_value('2')

    # press search button
    driver.find_element_by_css_selector('input[type="button"]').click()

    # Wait for rendering
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


    # Close driver
    driver.quit()


#test purpose
if __name__ == "__main__":
    main()
