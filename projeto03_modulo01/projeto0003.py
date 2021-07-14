def autoriza_voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    
    if idade > 18:
        print(f'Voce tem {idade} anos: VOTA!')
        return True 
    elif idade  >= 16 and idade > 65:
        print(f'Voce tem {idade} anos: VOTO OPCIONAL')
        return True 
    else:
        print (f'Voce tem {idade} anos: não vota')
        return False



candidatos = {
            '01': 'EU',
            '02': 'TU ',
            '03': 'ALGUEM',
            '04': 'Voto Nulo',
            '05': 'Voto Branco'
        }
while True :
    nasc = int(input('Digite o ano de nascimento: ou 0 para sair'))
    validacao = autoriza_voto(nasc)
    if validacao == True :
        print (candidatos)
        voto = input('Digite o número do candidato:  ')
        
    elif nasc == 0:
        break
    else:
        print ('voce infelizmente não pode votar')
        break

def votacao(votos):
    votos = {} # dicionário com total de votos começa vazio
    while True:
        
        
    #     if voto == 'fim':
    #         break # sai do while True
        if voto in candidatos: # se é um dos números de candidato válido
            votos[voto] = votos.get(voto, 0) + 1
        else:
            print(f'Número inválido: {voto}')

        print('Resultado:')
        for numero, qtd_votos in votos.items():
            print(f'{candidatos[numero]} teve {qtd_votos} votos') 