# tirar tudo de dentro da função e criar uma função recebe voto e idade ve se 
# a idade é valida para inputar o voto será que isso da certo? 


from datetime import date
atual = date.today().year
candidatos = {
    '1': 'Capitão Presença',
    '2': 'Super Aba ',
    '3': 'Malhado',
    '4': 'Voto Nulo',
    '5': 'Voto Branco'
}


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
            return autoriza_voto
        if idade >= 16 and idade <= 17:
            resposta = str(input('seu voto é opcional voce deseja votar? S/N \n')).upper()
            if resposta == "S":
                return autoriza_voto
            elif resposta == "N": 
                return check_age 

        else:
            print('infelizmente voce não pode votar')
            
    



    nas = int(input(f'Por favor inserir a data de nascimento do usuário  \n'))
    
    check_age(atual-nas)
    print(f'escolha seu canditado {candidatos}')
    voto = input('Digite o número do candidato: ')
    autoriza_voto(voto)







    # for numero, qtd_votos in votos.items():
    #     print(f'{candidatos[numero]} teve {qtd_votos} votos')
    # #print('Resultado:')