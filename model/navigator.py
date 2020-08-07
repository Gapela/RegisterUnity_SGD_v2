from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, visibility_of_element_located
from selenium.webdriver.common.by import By
from time import sleep

class NavigatorFunctions:
    def __init__(self, driver):
        sleep(2)
        self.driver = driver
        self.BTN_Backoffice = (By.XPATH, "/html/body/nav/div[1]/div/a[2]/button")
        self.BTN_UnidadesAcademicas = (By.XPATH, "/html/body/div[1]/div/div/div[1]/div/table/tbody/tr/td/input[14]")

#Actions
    def find(self, *locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(presence_of_element_located(*locator))
    def find_reduce(self, *locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(presence_of_element_located(*locator))
    def find_v(self, *locator, timeout=2):
        return WebDriverWait(self.driver, timeout).until(visibility_of_element_located(*locator))
    def frame_switch_id(self, id):
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_id(id))
    def frame_switch_parent(self):
        driver = self.driver
        driver.switch_to.parent_frame()
    def frame_switch_name(self, name):
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_name(name))
    def validar_click(self, clique_certo=None):
        try:
            self.find(clique_certo).click()
        except Exception as x:
            print(x)
            sleep(5)
            return self.validar_click(clique_certo)


#Functions
    def navigate_to_unities(self):
        self.validar_click(self.BTN_Backoffice)
        sleep(3)
        self.validar_click(self.BTN_UnidadesAcademicas)
        sleep(10)