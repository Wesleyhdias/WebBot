tabela = {'thead1': ['Período', 'Disciplina', '1° BIMESTRE', '2° BIMESTRE', 'Média Final', 'Frequência', 'Faltas', 'Situação'], 'thead2': ['PROVA1\n(8.0)', 'TRAB1\n(2.0)', 'SUB1\n(8.0)', 'MB1\n(10.0)', 'PROVA2\n(8.0)', 'TRAB2\n(2.0)', 'SUB2\n(8.0)', 'MB2\n(10.0)'], 'body': [['3º Semestre', 'ADMINISTRAÇÃO E ECONOMIA', '5.8', '2.0', '- - -', '7.8', '- - -', '- - -', '- - -', '- - -', '3.9', '100,00%', '0', 'Falta lançar alguma nota'], ['3º Semestre', 'CÁLCULO DIFERENCIAL E INTEGRAL III', '4.5', '2.0', '- - -', '6.5', '- - -', '- - -', '- - -', '- - -', '3.3', '100,00%', '0', 'Falta lançar alguma nota'], ['3º Semestre', 'CIRCUITOS DIGITAIS I', '6.7', '2.0', '- - -', '8.7', '- - -', '- - -', '- - -', '- - -', '4.4', '100,00%', '0', 'Falta lançar alguma nota'], ['3º Semestre', 'ESTATÍSTICA', '7.7', '2.0', '- - -', '9.7', '- - -', '- - -', '- - -', '- - -', '4.9', '100,00%', '0', 'Falta lançar alguma nota'], ['3º Semestre', 'FÍSICA II', '5.0', '2.0', '- - -', '7.0', '- - -', '- - -', '- - -', '- - -', '3.5', '100,00%', '0', 'Falta lançar alguma nota'], ['Média Geral: 4,00'], ['Frequência Média: 100,00']]}

print(tabela['thead1'])
print()
print(tabela['thead2'])
print()
for c in tabela['body']:
    print(f'{c}\n')