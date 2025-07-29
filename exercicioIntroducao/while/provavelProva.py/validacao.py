estadoCivilValido = [
    'c',
    's',
    'v',
    'd'
]

nome = input('Digite seu nome:')
while len(nome) <= 3:
    nome = input('Nome tem que ser maior que 3 caracteres TENTE NOVAMENTE:')

idade = int(input('Digite sua idade:'))
while (idade < 0) or (idade > 150):
    idade = int(input('Digite sua idade (tem que ser maior que zero e menor que 150):'))
    
salario = float(input('Digite o valor do seu salario: $'))
while salario <= 0:
    salario = float(input('salario precisa ser maior que zero: $'))

sexo = input('Digite seu Sexo (m, f):') 
while (sexo != 'm') and (sexo != 'f'):
    sexo = input('ERRO: sexo invalido. Digite seu Sexo (m, f): ')

estadoCivil = input('Digite seu estado civil (c, s, v, d):')
while estadoCivil not in estadoCivilValido:
    estadoCivil = input('ERRO estado civil não reconhecido! Digite seu estado civil (c, s, v, d):')


    

