#!/usr/bin/env python3
import email
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
#options.add_argument("--headless")
navegador = webdriver.Chrome(chrome_options=options)

equipe = {"isadora.silva": "7450Is@dora", "natanael.santos": "Natan2812@@", "jonathan.oliveira": "Indigocharj1", "guilherme.paulela": "guiguis2003", "samuel.souza": "41499686"}

def votacao(email, senha):
    time.sleep(5)
    navegador.get('https://app.feedz.com.br/')
    navegador.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/div/div/input').send_keys(f'{email}@think.br.com', Keys.TAB)
    navegador.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/div/div/input').send_keys(f'{senha}', Keys.ENTER)
    time.sleep(5)
    navegador.find_element_by_css_selector('img[src="/assets/images/mood-4.png"]').click()
    time.sleep(3)
    navegador.find_element_by_css_selector('button[class="fdz-btn fdz-btn-primary fdz-panel-mood-btn-submit"]').click()
    time.sleep(5)
    navegador.find_element_by_css_selector('button[class="confirm"]').click()
    time.sleep(5)
    navegador.find_element(By.XPATH, '/html/body/header/nav[1]/div/div/div[4]/button').click()
    time.sleep(5)
    navegador.find_element(By.XPATH, '/html/body/header/nav[1]/div/div/div[4]/ul/li[6]/a').click()
    time.sleep(3)

    mandar_email(email)

def mandar_email(email):
    time.sleep(5)
    navegador.get('https://outlook.office365.com/mail/')
    time.sleep(5)
    try:
        navegador.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]').send_keys('guilherme.paulela@think.br.com', Keys.ENTER)
        time.sleep(5)
        navegador.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input').send_keys('Gu1gu1$2003.', Keys.ENTER)
        time.sleep(5)
        navegador.find_element(By.XPATH, '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input').click()
    except:
        time.sleep(5)
    time.sleep(20)
    navegador.find_element_by_css_selector('i[data-icon-name="ComposeRegular"]').click()
    time.sleep(5)
    navegador.find_element_by_css_selector('input[role="combobox"]').send_keys(f'{email}@think.br.com', Keys.ENTER)
    navegador.find_element_by_css_selector('input[placeholder="Adicionar um assunto"]').send_keys('Enquete diária Feedz')
    navegador.find_element_by_css_selector('div[aria-label="Corpo da mensagem"]').send_keys('Bom dia,\n\nSua enquete diária foi respondida com êxito!', Keys.CONTROL + Keys.ENTER)

for i in range(len(equipe)):
    email 
    votacao(list(equipe)[i], list(equipe.values())[i])
    i += 1

navegador.quit()
print("FUNCIONOU!")

#{"natanael.santos": "Natan2812@@"}
#{"jonathan.oliveira": "Indigocharj1"}
#{"samuel.souza": "41499686"}
#{"isadora.silva": "7450Is@dora"}
#{"guilherme.paulela": "guiguis2003"}