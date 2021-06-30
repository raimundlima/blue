# tirar tudo de dentro da função e criar uma função recebe voto e idade ve se 
# a idade é valida para inputar o voto será que isso da certo? 

# from typing import Annotated
# from projeto03.maisum import autoriza_voto



# while True:
#     votos = {} # dicionário com total de votos começa vazio

#     def autoriza_voto():
        
#         if voto in candidatos: # se é um dos números de candidato válido
#             votos[voto] = votos.get(voto, 0) + 1
#         else:
#             print(f'Número inválido: {voto}')

def check_age ():
        from datetime import date
        atual = date.today().year
        idade = atual - nas
        if idade > 18:
            print('voce pode votar')
        if idade >= 16 and idade <= 17:
            resposta = str(input('seu voto é opcional voce deseja votar? S/N \n')).upper()
            if resposta == "S":
                return 'voce pode votar'
            elif resposta == "N": 
                return 'vaza'

        #else:
            #print('infelizmente voce não pode votar')
            
        


nas = int(input(f'Por favor inserir a data de nascimento do usuário  \n'))
    

    # print(f'escolha seu canditado {candidatos}')
    # voto = input('Digite o número do candidato: ')
    # autoriza_voto(voto)







    # for numero, qtd_votos in votos.items():
    #     print(f'{candidatos[numero]} teve {qtd_votos} votos')
    # #print('Resultado:')
