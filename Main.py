import pyautogui as py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
import pyperclip
import time
import pandas as pd
import openpyxl
import numpy
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Email

load_dotenv()

email = os.getenv("email")
password = os.getenv("password")

py.PAUSE = 0.5
py.alert("Do NOT touch the keyboard during operating. Thx")

# Step 1 - Access the company's system
# Initialize browser (Chrome) with detach option
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # 👈 keeps browser open
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--incognito")
browser = webdriver.Chrome(options=chrome_options)

# Open specific site
browser.get("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")

# Custom Settings
py.hotkey('win', 'up')

#Step 2 - Log in
# Login
time.sleep(1)
py.press('tab')
py.write('rique')

# Password
py.press('tab')
py.write('moretimeinthefrontofascreenmeansmoretimewithoutevertouchingascreenagain')
py.press('tab')
py.press('enter')

#Step 3 - Download the Data Base
time.sleep(3)
py.click(1181,339)
print("Arquivo baixado!")

#Step 4 - Calculate indicators

table = pd.read_csv(r"C:\Users\henrique_schorck\Downloads\Compras.csv", sep=";")
print(table)

'''
Total spent = sum of all row (ValorFinal)
Total ammount produced = sum of all row (Quantidade)
Average price = ValorFinal/Quantidade
'''

#variables in portuguese, as in the table
total_spent = table['ValorFinal'].sum()
quantity = table['Quantidade'].sum()
average_price = total_spent/quantity

print(f"Total spent = {total_spent}, Quantity = {quantity}, Average price = {average_price}")

#Step 5 - Send treated e-mail to another sector or directory 

# Navigate to Gmail
browser.get('https://accounts.google.com/')
time.sleep(2)

# Type email via Selenium (more natural to Google)
email_field = browser.find_element(By.ID, 'identifierId')
email_field.click()
email_field.send_keys(email)    
email_field.send_keys(Keys.ENTER)
time.sleep(3)

# Type password via Selenium
wait = WebDriverWait(browser, 30)
password_field = wait.until(EC.visibility_of_element_located((By.NAME, 'passwd')))
password_field.click()                       
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)
time.sleep(3)

py.hotkey('ctrl', 't')
py.write("https://www.gmail.com")
time.sleep(1)
py.press('enter')
time.sleep(8)
py.press('c')

py.write(Email.receiver_email)
time.sleep(1)
py.press(['enter','tab'])
time.sleep(1)
py.write(Email.email_title)
time.sleep(1)
py.press('tab')
py.write(Email.email_body)
time.sleep(1)
py.press(['tab', 'enter'])
