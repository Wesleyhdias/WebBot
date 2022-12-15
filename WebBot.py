from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def muda_xpath(xpath, oldstr, newstr, place=-1):
    xpath = xpath.split('/')
    xpath[place] = xpath[place].replace(str(oldstr), str(newstr))
    xpath = '/'.join(xpath)
    return xpath


def lista_texto(site, caminho, mserach='XPATH'):
    
    lista = []
    c = 1
    while True:
        try:
            v = site.find_element(By.XPATH, caminho)
        except NoSuchElementException:
            break
        except Exception as erro:
            print(f'tivemos um erro ainda não tratado\naqui está o erro\n\n{erro.__class__}\n')
            break
        else:
            caminho = muda_xpath(caminho, c, c+1)
            lista.append(v.text)
            c += 1

    return lista


def listas_texto(site, caminho, mserach='XPATH'):
    lista = []
    c = 1
    while True:
        v = lista_texto(site, caminho)
        if len(v) != 0:
            lista.append(v)
            caminho = muda_xpath(caminho, c, c+1, place = -2)
            c += 1
        else:
            break
        
    return lista


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

thead1 = lista_texto(web, '//*[@id="table-notas"]/thead/tr[1]/th[1]')
thead2 = lista_texto(web, '//*[@id="table-notas"]/thead/tr[2]/th[1]')
body = listas_texto(web, '//*[@id="table-notas"]/tbody/tr[1]/td[1]')

print(body)
