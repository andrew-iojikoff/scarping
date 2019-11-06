from selenium import webdriver
from selenium.common import exceptions as ex_
from bs4 import BeautifulSoup


class CommunityData():

    def __init__(self, communitiesName):
        self.communityName = communitiesName
        self.communities = []
        self.communities_data = []
        self.base_url = "https://pikabu.ru/communities/all"
        self.driver = webdriver.Chrome("c:/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(3)

    def get_communities_data(self):
        communities_soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        a = 1

    def get_communities_by_name(self):

        try:
            # найти поле ввода
            search_input = self.driver.find_element_by_class_name('communities-feed__search').find_element_by_class_name('input__input')
            # введем в поле ввода название сообщества
            search_input.send_keys(self.communityName)
            # найдем кнопку для отправки слова для поиска
            search_input_btn = self.driver.find_element_by_class_name('communities-feed__search').find_element_by_class_name('button_success')
            search_input_btn.click()
            search_end_block = self.driver.find_element_by_class_name('communities-feed__message')
            search_end_block_is_vis = search_end_block.is_displayed()

            while not search_end_block_is_vis:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.driver.implicitly_wait(3)
                search_end_block_is_vis = search_end_block.is_displayed()

            communities = self.driver.find_element_by_class_name('communities-feed__container').find_elements_by_class_name('community')

            for elem in communities:
                com = elem.find_element_by_class_name('community__title').find_element_by_tag_name('a')
                com_href = com.get_attribute('href')
                self.communities.append(com.get_attribute('href'))

        except ex_.NoSuchElementException:
            print("Сообществ с таким названием не существует")
            self.driver.close()
        return self.communities
