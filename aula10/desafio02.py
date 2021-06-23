from random import randint
jogador1 = []
computador = randint(0,3)
lista = ("Pedra", "Papel", "Tesoura")
jogar_novamente = "Sim"
while (jogar_novamente == "Sim"):
    jogador1 = int( input("escolha uma opção: \n [1] Pedra \n [2] Papel \n [3] Tesoura \n " ))
    
    if computador == 0:
        if jogador1 == 0:
            print("Empate! Ninguém ganhou." )
    elif jogador1 == 1 :
        print("Jogador perdeu." )
    elif jogador1 == 2 :
        print("o computador ganhou." )
else:
    print("Opção inválida tente novamente \n." )
jogar_novamente = input("Você quer tentar novamente? Digite Sim ou Não" )
print("Até a próxima!" )