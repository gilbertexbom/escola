# Cadastro de Estudantes

# Apresentação
print('\n\t\t\t -- Cadastro de Estudantes --\n')

estudante = {
    'Nome': 'Nome do estudante',
    'Curso':'Teste',
    'Nota':0,
    'Matricula':False
}

# Entrada
estudante['Nome'] = input('Informe o nome do estudante: ')
estudante['Nota'] = float(input('Informe a nota: '))
estudante['Curso'] = input('Informe o curso: ')
matricula = input('Estudante regular (s/n)? ')
if matricula.lower() == 's':
    estudante['Matricula'] = True



# Saída
print(f'\n\nNome...................{estudante["Nome"]}')
print(f'Curso..................{estudante["Curso"]}')
print(f'Nota...................{estudante["Nota"]}')
print('Estudante Regular') if estudante['Matricula'] else print('Matricula Trancada')
# print(f'Matricula...............{estudante["Matricula"]}')

