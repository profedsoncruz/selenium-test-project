import time
from selenium import webdriver
from page_objects import PageObject, PageElement


class Google(PageObject):
    search_bar = PageElement(id_='lst-ib')
    btn_search = PageElement(name='btnK')
    btn_lucky = PageElement(name='btnI')
    g_logo = PageElement(id_='hplogo')

    def search(self, text):
        self.search_bar.send_keys(text)
        self.g_logo.click()
        self.btn_search.click()

    def lucky(self, text):
        self.search_bar.send_keys(text)
        self.g_logo.click()
        self.btn_lucky.click()


browser = webdriver.Chrome()
g = Google(browser, 'http://www.google.com.br/')
g.get('')
time.sleep(3)
g.search('Universidade Positivo')
time.sleep(20)
g.get('')
time.sleep(3)
g.lucky('Pós Graduação Testes de Software da Universidade Positivo')
