nome = input('Digite o nome de usuário: ')
senha = input('Crie uma senha: ')

while senha == nome:
    senha = input('A senha NÃO pode ser igual ao nome de usuário\nTente Novamente:')

print('Cadastro feito com SUCESSO')