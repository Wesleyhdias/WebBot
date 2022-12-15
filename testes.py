xpath = '//*[@id="table-notas"]/tbody/tr[1]/td[1]'
place = -1
c = 1
oldstr = c
newstr = c+1



for a in range(10):
    xpath = xpath.split('/')
    xpath[place] = xpath[place].replace(str(oldstr), str(newstr))
    xpath = '/'.join(xpath)
    c += 1
    oldstr = c
    newstr = c+1
    print(f'{xpath}')
