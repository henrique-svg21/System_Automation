import pyautogui as py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 👈 add this import
import pyperclip
import time
import pandas as pd
import openpyxl
import numpy

py.PAUSE = 0.5
py.alert("Do NOT touch the keyboard during operating. Thx")

# Step 1 - Access the company's system
# Initialize browser (Chrome) with detach option
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # 👈 keeps browser open
browser = webdriver.Chrome(options=chrome_options)

# Open specific site
browser.get("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")

# Custom Settings
py.hotkey('win', 'up')

#Step 2 - Log in
# Login
py.press('tab')
py.write('rique')

# Password
py.press('tab')
py.write('quantomaistemponafrentedopcmaioravontadedenuncamaistocaremumcomputadornaminhavida')
py.press('tab')
py.press('enter')

#Step 3 - Download the Data Base
time.sleep(3)
py.click(1181,339)
print("Arquivo baixado!")
time.sleep(3)
py.hotkey('alt', 'f4')

#Step 4 - Calculate indicators

table = pd.read_csv(r"C:\Users\henrique_schorck\Downloads\Compras.csv", sep=";")
print(table)


