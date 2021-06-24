from datetime import date
candidatos = {
    '01': 'Capitão Presença',
    '02': 'Super Aba ',
    '03': 'Malhado',
    '04': 'Voto Nulo',
    '05': 'Voto Branco'
}
nas = int(input('Por favor insira sua data de nascimento \n'))

print (f'escolha seu canditado {candidatos}')
votos = {} # dicionário com total de votos começa vazio
while True:
    voto = input('Digite o número do candidato (ou "fim" para encerrar): ')
    if voto == 'fim':
        break # sai do while True
    if voto in candidatos: # se é um dos números de candidato válido
        votos[voto] = votos.get(voto, 0) + 1
    else:
        print(f'Número inválido: {voto}')

print('Resultado:')
for numero, qtd_votos in votos.items():
    print(f'{candidatos[numero]} teve {qtd_votos} votos')


atual = date.today().year
def check_age (idade):
    
    idade = atual - nas
    if idade > 18:
            print('seu voto é obrigatório')
    elif idade >= 16 and idade <= 17:
            print ('seu voto é opcional')
    else:
            print ('voce não pode votar ')


check_age(atual-nas)