from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import os
import requests
import json
import wget


url = "https://app.ekodevices.com/login"
login = "clarissa.lima@academico.ufpb.br"
senha = "12denovembro"
dire = os.getcwd()
nome_paciente = "Cleilton a"


# ### DRIVER CONFIG
# def _driver():
#     chrome_options = webdriver.ChromeOptions()
#     prefs = {'download.default_directory' : dire}
#     chrome_options.add_experimental_option('prefs', prefs)
#     driver = webdriver.Chrome(executable_path = f"{dire}\\chromedriver.exe", chrome_options = chrome_options)
#     driver.maximize_window()
#     return driver

# driver = _driver()
# wait = WebDriverWait(driver, 15)
# driver.get(url)

# ### LOGIN
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))).send_keys(login) 
# driver.find_element(by = By.XPATH, value = '//*[@id="password"]').send_keys(senha)   
# sleep(0.5)
# driver.find_element(by = By.XPATH, value = '//*[@id="__next"]/div/div[1]/div[2]/div/form/button[1]').click() 
 
# ### PATIENTS
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/nav/div/div[2]/div/ul/li[2]/a'))).click()

# ### NOME PACIENTE
# wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'css-18g0ywd')))
# [x.click() for x in driver.find_elements(By.CLASS_NAME, 'css-18g0ywd') if nome_paciente in x.text]

# ### GRAVAÇÃO MAIS RECENTE
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/main/div[1]/div[1]/div')))
# wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-18g0ywd'))).click()

# ### DOWNLOADS
# sleep(10)
# while True:
#     try:
#         l = [x for x in driver.find_elements(By.XPATH, '//*[@type="button"]') if 'Download' in x.text]
#     except:
#         print("erro")
#         continue
#     break


cookies = {'__Secure-next-auth.session-token': 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..V-gtsd0QscJ1zPNI.DEvdGqmNUhyyfjlDY50HY2c84T471i0bd9i9F2mXnIZiQo7Q9xd9tHF42CkybqX2JbyI6-eFNvvoczCo8wdFwajPEmc7Dw8uaoCuN3qm0cPo9mo_5_-z68ydBIY2pMjG5JnMTOESdy_yVjDwymrs9McbbTZOpfAp3v8H5Bm82npDREkInXkvpev6sjOi8ec-Y1zNCFv_atvJH9piTv1faQtcKfFLfUn1D42FbpGkC42hmVIbqVQUmHjy88vguPosePHOM7LYolWQ0nuM0hZ823edolyQ401lBzCZlfQWSYnzUq57zaYHPSRQftRKpE2_0H9uB1LCwVOxiiUz2g1R0Mc5PbxlvN-LU-Cht4RhoySfqB2lr37FcjH0t7eX8OFm8ZPf14hddHMjV-EPScfK_3mEIM8oISavqO4n_-Wn_t8MIRtTxURjEQ2zt4zGgabpy2O23n1iSYjyySfymuzrAUhIG-i34SSEx1yIggcKkbO112pVCc_E4cLo_OCOKxeRkKk05x5sVblppDF4GBMAISQ_23rPtqF8kr8NJPrR2_InNGLK5imqL49xbYUP0RFWLngmkMOq5ci7EVa_-S8bZBEWZVLbT5uxHHCBl7vs2ecSTjBLe4a2bVDLw4Z5br0Si1RVAMUVzS_FP2FgafL4YeQY-mlAjbcCL4Iak-_gCwJKtruOoPqp-uuelckH0ayzJI1ImPFlvIfBQW8ICYOO_3vK50Yyg4LgOWL2y1Zv4Gj4ixALHzFMY3WsCYT-mqLbc2n9k2MimzD8GK4xP-3VVdBi.BEI7rh0XbgcbELEo-yab6w',
           'mp_505d769187fd7cb5be39d0b4dd21da34_mixpanel':'%7B%22distinct_id%22%3A%20%22245455%22%2C%22%24device_id%22%3A%20%221859bd034f74c0-0ec90d04506b2d-26021151-100200-1859bd034f861b%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20%22245455%22%7D'}

url = 'https://app.ekodevices.com/api/v3/recordings/38a4d026-9c79-49bc-823d-b5de5d9fcef9?show_as_pdf=true'
# url = f'https://app.ekodevices.com/api/v3/recordings/{driver.current_url.split("/")[-1]}'

r = requests.get(url, cookies = cookies)
# j = json.loads(r.content)
# wget.download(j["amazon_url_audio_filtered"], f"{dire}//{nome_paciente}.wav")
