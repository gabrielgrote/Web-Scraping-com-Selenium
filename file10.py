from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# '/home/graciela/anaconda3/chromedriver'
'''
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
'''

searchWord = input("O que voce quer pesquisar no Mercado Livre: ")

driver = webdriver.Chrome()
driver.get('https://lista.mercadolivre.com.br/'+searchWord)

products = driver.find_element_by_class_name('ui-search-results')

section = driver.find_element_by_class_name('ui-search-results')

ols = section.find_elements_by_tag_name('ol')
counter = 0

for ol in ols:
    ol = ol.find_elements_by_tag_name('li')
    for li in ol:
        counter = counter + 1
        asdf3 = li.find_element_by_class_name('ui-search-result__content')
        asdf5 = asdf3.find_element_by_tag_name('h2')
        asdf4 = asdf3.find_element_by_class_name('price-tag')
        asdf6 = asdf4.find_element_by_class_name('price-tag-text-sr-only')
        print(asdf5.text)
        print(asdf6.text)
        print("========")
