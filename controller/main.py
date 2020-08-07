from model.excel import ExcelFunctions
from model.navigator import NavigatorFunctions
from model.user import UserFunctions
from selenium import webdriver

#Selenium webdriver
url = 'http://sgd2.lab245.com.br/'
bot = webdriver.Firefox()
bot.get(url)

#Instances
excel = ExcelFunctions(bot)
user = UserFunctions(bot)
navigator = NavigatorFunctions(bot)

#Functions
excel.import_excel()
user.user_autentication()
navigator.navigate_to_unities()
excel.register_unidades()

bot.close()