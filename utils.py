from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from time import sleep


def muda_xpath(xpath, oldstr, newstr, place=-1):
    xpath = xpath.split('/')
    xpath[place] = xpath[place].replace(str(oldstr), str(newstr))
    xpath = '/'.join(xpath)
    return xpath


def txt_list(site, caminho, mserach='XPATH'):
    
    global res
    res = ''
    lista = []
    c = 1
    while True:
        try:
            v = site.find_element(By.XPATH, caminho)
            lista.append(v.text)
        except NoSuchElementException:
            if len(lista) != 0:
                res = 'encontrei respostas'
                break
            else:
                res = 'nada encontrado'
                break
        except NoSuchWindowException:
            print(lista, len(lista))
            break
        except AttributeError:
            break
        except Exception as erro:
            print(f'tivemos um erro ainda não tratado\naqui está o erro\n\n{erro.__class__}\n')
            break
        else:
            caminho = muda_xpath(caminho, c, c+1)
            c += 1
    if res == 'encontrei respostas':
        return lista
    else:
        return False

def txt_lists(site, caminho, mserach='XPATH'):
    global res
    lista = []
    c = 1
    while True:
        v = txt_list(site, caminho)
        if v == False and len(lista) == 0:
            return False
        elif v == False and len(lista) != 0:
            return lista
        else:
            lista.append(v)
            caminho = muda_xpath(caminho, c, c+1, place = -2)
            c += 1


def get_grades(site, login, senha, toStr):
    options = Options()
    options.headless = False
        
    service = Service(ChromeDriverManager().install())
    web = webdriver.Chrome(service=service, options=options)

    web.get(site)
    web.find_element(By.ID, 'login').send_keys(login)
    web.find_element(By.ID, 'senha').send_keys(senha)
    web.find_element(By.ID, 'btn-login').click()
    web.find_element(By.XPATH, '//*[@id="layout-sidenav"]/ul/li[2]/a').click()
    sleep(0.2)
    web.find_element(By.XPATH, '//*[@id="layout-sidenav"]/ul/li[2]/ul/li[1]').click()
    sleep(0.5)

    body = txt_lists(web, '//*[@id="table-notas"]/tbody/tr[1]/td[1]')
    
    provaB1 = []
    provaB2 = []
    subB1 = []
    subB2 = []
    trabB1 = []
    trabB2 = []
    materias = []

    for c in body:
        if len(c) >= 2:
            materias.append(c[1])
            provaB1.append(c[2])
            trabB1.append(c[3])
            subB1.append(c[5])
            provaB2.append(c[6])
            trabB2.append(c[7])
            subB2.append(c[8])
    
    tabela = [materias, provaB1, trabB1, subB1, provaB2, trabB2, subB2]
    
    if toStr == True:
        for k, v in enumerate(tabela):
            v = '\n'.join(v)
            tabela[k] = v
    
    return tabela
