    
# def autoriza_voto():
#     from datetime import date
#     ano = 0
#     atual = date.today().year
#     idade = atual - ano
    
#     if idade < 16:
#         return f'Voce tem {idade} anos: NÃO VOTA!'
    #elif idade 16 <= or <18 or idade > 65:
#         return f'Voce tem {idade} anos: VOTO OPCIONAL'
#     else:
#         return f'Voce tem {idade} anos: VOTO OBRIGATÓRIO'


# while nas > 16 :
#     pass
# else:
#     print('voce não pode continuar')

candidatos = {
            '01': 'Capitão Presença',
            '02': 'Super Aba ',
            '03': 'Malhado',
            '04': 'Voto Nulo',
            '05': 'Voto Branco'
        }
def votacao (votos):


    
    votos = {} # dicionário com total de votos começa vazio
    voto = input('Digite o número do candidato (ou "fim" para encerrar): ')
    if voto in candidatos: # se é um dos números de candidato válido
            votos[voto] = votos.get(voto, 0) + 1
    else:
            print(f'Número inválido: {voto}')

    print('Resultado:')
    for numero, qtd_votos in votos.items():
        print (f'escolha seu canditado {candidatos}')
        print(votacao)
        print(f'{candidatos[numero]} teve {qtd_votos} votos')    


# programa principal
#nas = int(input('em que ano voce nasceu? \n'))
