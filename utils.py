from selenium import webdriver
from selenium.webdriver.common.by import By
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
    
    lista = []
    c = 1
    while True:
        try:
            v = site.find_element(By.XPATH, caminho)
            lista.append(v.text)
        except NoSuchElementException:
            if len(lista) == 0:
                print("esse caminho não possui nenhum elemento...")
                break
            else:
                break
        except NoSuchWindowException:
            print(lista, len(lista))
            break
        except Exception as erro:
            print(f'tivemos um erro ainda não tratado\naqui está o erro\n\n{erro.__class__}\n')
            break
        else:
            caminho = muda_xpath(caminho, c, c+1)
            c += 1
    if len(lista) == 0:
        return 'nenhum elemento encontrado'
    else:
        return lista


def txt_lists(site, caminho, mserach='XPATH'):
    lista = []
    c = 1
    while True:
        v = txt_list(site, caminho)
        if v == 'nenhum elemento encontrado':
            break
        elif len(v) != 0:
            lista.append(v)
            caminho = muda_xpath(caminho, c, c+1, place = -2)
            c += 1
    if v == 'nenhum elemento encontrado':
        return v
    else:
        return lista


def get_grades(site, login, senha):
    service = Service(ChromeDriverManager().install())
    web = webdriver.Chrome(service=service)

    web.get(site)
    web.find_element(By.ID, 'login').send_keys(login)
    web.find_element(By.ID, 'senha').send_keys(senha)
    web.find_element(By.ID, 'btn-login').click()
    web.find_element(By.XPATH, '//*[@id="layout-sidenav"]/ul/li[2]/a').click()
    sleep(0.2)
    web.find_element(By.XPATH, '//*[@id="layout-sidenav"]/ul/li[2]/ul/li[1]').click()
    sleep(0.5)

    thead1 = txt_list(web, '//*[@id="table-notas"]/thead/tr[1]/th[1]')
    thead2 = txt_list(web, '//*[@id="table-notas"]/thead/tr[2]/th[1]')
    body = txt_lists(web, '//*[@id="table-notas"]/tbody/tr[1]/td[1]')
    
    if body or thead1 or thead2 == 'nenhum elemento encontrado':
        return body
    else:
        # quando tiver notas no site contruir uma tabela com elas e dar como o valor de retirno dessa função
        tabela = {'thead1': thead1, 'thead2': thead2, 'body': body}
    
        return tabela
    


# não tem mais notas no site :/
# vai ficar travado aqui um tempo.