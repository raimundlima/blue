import random

ask = int(input('''Escolha uma opcao para se jogar: 

[0] Pedra
[1] Papel
[2] Tesoura
 
Digite sua escolha: '''))
computador = random.randint(0,2)

if computador == 0:
    print('O computador escolheu: Pedra')
    if ask == 0:
        print("Empate!")
    elif ask == 1:
        print("Voce perdeu")
    elif ask == 2:
        print("Computador venceu")
    else:
        print("A sua opção é invalida!")
        
elif computador == 1:
    print('O computador escolheu: Papel')
    if ask == 0:
        print("Computador perdeu")
    elif ask == 1:
        print("Empate!")
    elif ask == 2:
        print("Voce venceu")
    else:
        print("Operacao invalida")
elif computador == 2:
    print('O computador escolheu: Tesoura')
    if ask == 0:
        print("Jogador venceu")
    elif ask == 1:
        print("Computador venceu")
    elif ask == 2:
        print("Empate!")
    else:
        print("Operacao invalida")
else:
    print("Operacao invalida")


