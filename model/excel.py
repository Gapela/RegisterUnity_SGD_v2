import pandas as pd
from tkinter.filedialog import askopenfilename
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, visibility_of_element_located
from time import sleep

class ExcelFunctions:
    def __init__(self, driver):
        self.driver = driver
        self.BTN_Listar = (By.XPATH, "/html/body/center/form/table/tbody/tr[3]/td[2]/input[1]")
        self.BTN_Incluir = (By.XPATH, "/html/body/center/form/table/tbody/tr[3]/td[2]/input[2]")
        self.FIELD_Polos = (By.NAME, "Valor1")
        self.FIELD_Instituicao = (By.NAME, "Valor2")
        self.FRAME_iframe = "_iframe"
        self.FRAME_dica = "dica"
        self.MSG_F245Mensagem = (By.CLASS_NAME, "F245Mensagem")
        self.MSG_NotFound_CSS = (By.CSS_SELECTOR, "body > font > b")
        self.status = False

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

    def click_Incluir(self):
        self.find_v(self.BTN_Incluir)
        self.validar_click(self.BTN_Incluir)
        print("   Incluido")

    def click_Listar(self):
        self.find_v(self.BTN_Listar)
        self.validar_click(self.BTN_Listar)

#Functions
    def import_excel(self):
        self.filename = askopenfilename(initialdir="C:/", title="select file")
        self.wb = pd.read_excel(self.filename)
        self.polos = self.wb['POLOS'].values.tolist()
        self.ies = self.wb['IES'].values.tolist()

        self.unidades_qtd = len(self.wb)

    def calculate_progress(self, i):
        self.i = i + 1
        self.progress = (self.i * 100) / self.unidades_qtd
        print("-------------------------------- " + str(round(self.progress, 1)) + "%")
        sleep(1)

    def validate_unity(self):
        try:
            self.frame_switch_name(self.FRAME_dica)
            self.element = self.find_reduce(self.MSG_F245Mensagem)
            self.msgNotFoud = self.element.text
        except:
            print("   Status: Encontrado")
            self.status = True
            self.frame_switch_parent()
            sleep(2)
        else:
            print("   Status: Não Encontrado")
            self.status = False
            self.frame_switch_parent()
            sleep(2)

    def register_unidades(self):
        if (self.status == False):
            self.click_Incluir()

    def search_unidades(self, i):
        print(str(i + 1) + ". Polo: " + str(self.polos[i]))
        print("   Ies: " + str(self.ies[i]))

        self.find(self.FIELD_Polos).clear()
        self.find(self.FIELD_Instituicao).clear()

        self.find(self.FIELD_Polos).send_keys(self.polos[i])
        self.find(self.FIELD_Instituicao).send_keys(self.ies[i])

        self.click_Listar()
        sleep(1)
        self.click_Listar()
        sleep(3)

    def module_unidades(self):
        print("Starting Registration...\n")

        print("Unity quantity: " + str(self.unidades_qtd) + "\n")

        self.frame_switch_id(self.FRAME_iframe)
        for i in range(self.unidades_qtd):
            self.search_unidades(i)
            self.validate_unity()
            self.register_unidades()
            self.calculate_progress(i)
