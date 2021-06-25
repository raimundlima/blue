
from datetime import date
atual = date.today().year
candidatos = {
    '1': 'Capitão Presença',
    '2': 'Super Aba ',
    '3': 'Malhado',
    '4': 'Voto Nulo',
    '5': 'Voto Branco'
}

check = [0]
while True:
    votos = {} # dicionário com total de votos começa vazio

    def autoriza_voto(voto):
        
        if voto in candidatos: # se é um dos números de candidato válido
            votos[voto] = votos.get(voto, 0) + 1
        else:
            print(f'Número inválido: {voto}')

    def check_age (idade):
        
        idade = atual - nas
        if idade > 18:
            return (autoriza_voto)
        if idade >= 16 and idade <= 17:
            resposta = str(input('seu voto é opcional voce deseja votar? S/N \n')).upper()
            if resposta == "S":
                return (autoriza_voto)
            elif resposta == "N": 
                return (check_age)

        elif idade <=15 :
            print('infelizmente voce não pode votar')
    



    nas = int(input(f'Por favor inserir a data de nascimento do usuário  \n'))
    # if check == 0:
    #     break
    check_age(atual-nas)
    print(f'escolha seu canditado {candidatos}')
    voto = input('Digite o número do candidato: ')
    autoriza_voto(voto)







    # for numero, qtd_votos in votos.items():
    #     print(f'{candidatos[numero]} teve {qtd_votos} votos')
    # #print('Resultado:')