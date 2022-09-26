import os
import smtplib
from email.message import EmailMessage

# email = ''
# senha = ''

# Imports to read excel
import pandas as pd  # pd as a name to call method pandas on my code

import time
# Automate on web
from selenium import webdriver  # Manipulate the google chrome browser
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # Find the elements
from selenium.webdriver.common.keys import Keys  # Write on web keyboard

# 1 - Read the file

file_name = "rr01br00049.xlsx"
df = pd.read_excel(file_name)
url_claw = "https://claw.scania.com/default.aspx"

# print(df)

for index, row in df.iterrows():
    # print('Posição: ' + str(index) + '\n' +  'Usuário: ' + row["USUARIO"])

    # #Descontinued
    # chrome = webdriver.Chrome(executable_path='chromedriver.exe') #Create instance and put in variable "chrome"

    # DEFAULT
    ser = Service("chromedriver.exe")
    op = webdriver.ChromeOptions()
    chrome = webdriver.Chrome(service=ser, options=op)
    chrome.get(url_claw)
    #######################################

    time.sleep(3)

    user = chrome.find_element(By.XPATH, '//*[@id="txtUsername"]')
    passwd = chrome.find_element(By.XPATH, '//*[@id="txtPassword"]')
    login = chrome.find_element(By.XPATH, '//*[@id="cmdSignIn"]')
    # login_error = chrome.find_element(By.XPATH, '//*[@id="message-holder-error"]')
    # login_information = chrome.find_element(By.XPATH, '//*[@id="message-holder-information"]')

    user.send_keys(row["USUARIO"])  # Set user on field
    passwd.send_keys(row["SENHA"])  # Set password on field
    login.click()  # Click to enter on the system

    time.sleep(3)

    # if login_error == True:
    #     # Close browser
    #     chrome.close()
    #     print("Alert: Login error!!!")
    # elif login_information == True:
    #     # Close browser
    #     chrome.close()
    #     print("Alert: Login error!!!")
    # else:
    #     chrome.close()
    #     print("Login successfully!!!")
