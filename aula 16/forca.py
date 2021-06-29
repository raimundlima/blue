from random import choice

quantidade_erros_atual = 0
quantidade_erros_jogo = 6 # quantidades de vezes que o usuário pode errar 

palavras = ['lixeira','circo','pneu','maremoto','vendaval','alegremente','condicional']
letras_erradas = []
letras_certas = []

palavra = choice(palavras).lower()
palavra_exibicao = list(' _ ' * len(palavra))
print ('Bem vindo(a) ao jogo da forca!!!')
print(f'Vc pode cometer até {quantidade_erros_jogo-1} erros, ou seja no erro número {quantidade_erros_jogo}')

while quantidade_erros_atual < quantidade_erros_jogo and ' _ ' in palavra_exibicao:
    print('Palavra:', ' _ '.join(palavra_exibicao))
    print(f'Status: {quantidade_erros_atual} de {quantidade_erros_jogo} erros')
    print(f'Letras erradas: {" _ ".join(letras_erradas)}')
    letra = input('Digite uma letra:').lower()
# palavras = ['arroz','batata','aspas','lista','nebuloso']
# palavras_sorteada = random.choice(palavras)
# #print(palavras_sorteada)
# #print(len(palavras_sorteada))
# print(' _ ' * len(palavras_sorteada))