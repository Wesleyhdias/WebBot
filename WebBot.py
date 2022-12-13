from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

service = Service(ChromeDriverManager().install())
web = webdriver.Chrome(service=service)

web.get("https://feitep.jacad.com.br/academico/aluno-v2/login")
web.find_element(By.ID, 'login').send_keys('4245')
web.find_element(By.ID, 'senha').send_keys('09052004')
web.find_element(By.ID, 'btn-login').click()
web.find_element(By.XPATH, '//*[@id="layout-sidenav"]/ul/li[2]/a').click()
sleep(0.1)
web.find_element(By.XPATH, '//*[@id="layout-sidenav"]/ul/li[2]/ul/li[1]').click()
sleep(0.5)


tabela_completa = web.find_element(By.XPATH, '//*[@id="table-notas"]')
thead1 = web.find_element(By.XPATH, '//*[@id="table-notas"]/thead/tr[1]')
thead2 = web.find_element(By.XPATH, '//*[@id="table-notas"]/thead/tr[2]')
tbody = web.find_element(By.XPATH, '//*[@id="table-notas"]/tbody')

sleep(0.5)

print(f'tabela completa\n{tabela_completa.text}\n\nthead1:\n{thead1.text}\n\nthead2:\n{thead2.text}\n\nbody:\n{tbody.text}')

# arrumar um jeito de organizar os valores tirados do site de forma que facilite a manipulação, tentar usar listas e dicionarios.
