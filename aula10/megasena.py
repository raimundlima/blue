from random import randint

q_jogos = int(input("Quantos jogos voce quer gerar? \n"))

jogos_total = list()

for i in range(q_jogos): #quantidades de jogos que o usuario solicitou 
    jogo = list() #zera a lista quando o jogo tiver 6 
    while len(jogo) <6 : # enquanto minha lista for menor do que 6, repito o bloco 
        num = randint(1, 60)
        if num not in jogo: # só armazena se o numero se não estiver na lista 
            jogo.append(num) #coloca o que estiver armazenado em "num" no final da minha lista 
    jogos_total.append(jogo)    
print(jogos_total)
