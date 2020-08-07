from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, visibility_of_element_located

class UserFunctions:
    def __init__(self, driver):
        self.driver = driver
        self.LOGIN = (By.ID, "txtLogin")
        self.SENHA = (By.ID, "txtSenha")

    #Actions
    def find(self, *locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(presence_of_element_located(*locator))

#Getters and Setters
    #login
    def set_login(self):
        self.login = "gabriel.pelai.ter"
        #self.login = input("Insira seu login: ")

    def get_login(self):
        return self.login

    #senha
    def set_senha(self):
        self.senha = ("Gp4e129757")
        #self.senha = input("Insira sua senha: ")

    def get_senha(self):
        return self.senha

#Function
    def user_autentication(self):
        self.set_login()
        self.set_senha()
        self.find(self.LOGIN).send_keys(self.get_login())
        self.find(self.SENHA).send_keys(self.get_senha())
        self.find(self.SENHA).send_keys(Keys.ENTER)