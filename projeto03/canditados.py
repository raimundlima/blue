
candidatos = {
    '01': 'Capitão Presença',
    '02': 'Super Aba ',
    '03': 'Malhado',
    '04': 'Voto Nulo',
    '05': 'Voto Branco'
}


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


# candidatos = {
#     '1': 'Capitão Presença',
#     '2': 'Super Aba ',
#     '3': 'Malhado',
#     '4': 'Voto Nulo',
#     '5': 'Voto Branco'
# }
# votos = {} # dicionário com total de votos começa vazio
# def autoriza_voto(voto):
#     if voto in candidatos: # se é um dos números de candidato válido
#         votos[voto] = votos.get(voto, 0) + 1
#     else:
#         print(f'Número inválido: {voto}')
# print(f'escolha seu canditado {candidatos}')
# voto = input('Digite o número do candidato: ')
# autoriza_voto(voto)
# #print('Resultado:')
# #for numero, qtd_votos in votos.items():
# #     print(f'{candidatos[numero]} teve {qtd_votos} votos')

