import pandas as pd

cont = 0
colb1 = []
colb2 = []
predat = []
datb1 = []
datb2 = []
tabela = [['Período', 'Disciplina', '1° BIMESTRE', '2° BIMESTRE', 'Média Final', 'Frequência', 'Faltas', 'Situação'], ['PROVA1\n(8.0)', 'TRAB1\n(2.0)', 'SUB1\n(8.0)', 'MB1\n(10.0)', 'PROVA2\n(8.0)', 'TRAB2\n(2.0)', 'SUB2\n(8.0)', 'MB2\n(10.0)'], [['3º Semestre', 'ADMINISTRAÇÃO E ECONOMIA', '5.8', '2.0', '- - -', '7.8', '- - -', '- - -', '- - -', '- - -', '3.9', '100,00%', '0', 'Falta lançar alguma nota'], ['3º Semestre', 'CÁLCULO DIFERENCIAL E INTEGRAL III', '4.5', '2.0', '- - -', '6.5', '- - -', '- - -', '- - -', '- - -', '3.3', '100,00%', '0', 'Falta lançar alguma nota'], ['3º Semestre', 'CIRCUITOS DIGITAIS I', '6.7', '2.0', '- - -', '8.7', '- - -', '- - -', '- - -', '- - -', '4.4', '100,00%', '0', 'Falta lançar alguma nota'], ['3º Semestre', 'ESTATÍSTICA', '7.7', '2.0', '- - -', '9.7', '- - -', '- - -', '- - -', '- - -', '4.9', '100,00%', '0', 'Falta lançar alguma nota'], ['3º Semestre', 'FÍSICA II', '5.0', '2.0', '- - -', '7.0', '- - -', '- - -', '- - -', '- - -', '3.5', '100,00%', '0', 'Falta lançar alguma nota'], ['Média Geral: 4,00'], ['Frequência Média: 100,00']]]

for c in tabela[2]:
    for k, v in enumerate(c):
        if k > 1 and k < 10:
            predat.append(v)
        if k == 5:
            datb1.append(predat)
            predat = []
        elif k == 9:
            datb2.append(predat)
            predat = []

for c, v in enumerate(tabela[1]):
    predat.append(v)
    if c == 3:
        colb1.append(predat)
        predat = []
    elif c == 7:
        colb2.append(predat)
        predat = []

dfb1 = pd.DataFrame(data= datb1, columns=colb1)
dfb2 = pd.DataFrame(data= datb2, columns=colb2)
print(f'{dfb1}\n\n{dfb2}')