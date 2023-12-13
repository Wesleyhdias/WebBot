from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image, ImageDraw, ImageFont
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from time import sleep
import os


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
        
    web = webdriver.Chrome()

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
    medB1 = []
    medB2 = []
    materias = []

    for c in body:
        if len(c) >= 2:
            materias.append(c[1])
            provaB1.append(c[2])
            trabB1.append(c[3])
            subB1.append(c[4])
            medB1.append(c[5])
            provaB2.append(c[6])
            trabB2.append(c[7])
            subB2.append(c[8])
            medB2.append(c[9])
    
    tabela = [materias, provaB1, trabB1, subB1, medB1, provaB2, trabB2, subB2, medB2]
    
    if toStr == True:
        for k, v in enumerate(tabela):
            v = '\n'.join(v)
            tabela[k] = v
    
    return tabela


def drawText(matriz):
    
    
    for i, c in enumerate(matriz[0]):
        if len(c) >= 20:
            p2 = []
            c = c.split(' ')
            if len(c[0] + ' ' + c[1]) >= 15:
                p1 = c[0] + ' ' + c[1]
                for j in range(2, len(c)):
                    p2.append(c[j])
                p2 = ' '.join(p2) 
            else:
                p1 = c[0] + ' ' + c[1] + ' ' + c[2]
                for j in range(3, len(c)):
                    p2.append(c[j])
                p2 = ' '.join(p2) 
            matriz[0][i] = p1 + '\n' + p2
                

    defalt_dir = os.path.dirname(__file__)
    gradeSheet_dir = os.path.join(defalt_dir, "gradeSheet.png")	

    font = ImageFont.truetype('MONOCRAFT.OTF', 33)

    img = Image.open(gradeSheet_dir)
    drawImg = ImageDraw.Draw(img)

    for i, colun in enumerate(matriz):
        for j, lin in enumerate(colun):
            if i == 0:
                drawImg.text((175, 430+(j*88)), lin, (0, 0, 0), font=font, anchor="la")
            else:
                drawImg.text((610+(i*175), 452+(j*88)), lin, (0, 0, 0), font=font, anchor="la")

    img.save('notas.png')
