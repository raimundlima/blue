flag = True
ze = 1
maria = 2
joao = 3
tereza = 4
nulo = 5
branco = 6
vZe = 0
vMaria = 0
vJoao = 0
vTereza = 0
vNulo = 0
vBranco = 0
vTotal = 0
mensagemVoto = "Obrigado pelo seu voto!"
mensagemEncerra = "Voto encerrado!"

while flag:
    sn = input("\nVocê deseja votar? ")
    while True:
        if sn[0].lower() == "s":
            print("""
=-=-=-=-=-=-=-=-=-=-=
[1] - Zé
[2] - Maria
[3] - João
[4] - Tereza
[5] - Voto Nulo
[6] - Voto em Branco
=-=-=-=-=-=-=-=-=-=-=""")
            voto = int(input("Qual é o seu voto? "))
            if voto == ze:
                vZe += 1
                vTotal += 1
                print(mensagemVoto)
                break
            elif voto == maria:
                vMaria += 1
                vTotal += 1
                print(mensagemVoto)
                break
            elif voto == joao:
                vJoao += 1
                vTotal += 1
                print(mensagemVoto)
                break
            elif voto == tereza:
                vTereza += 1
                vTotal += 1
                print(mensagemVoto)
                break
            elif voto == nulo:
                vNulo += 1
                vTotal += 1
                print(mensagemVoto)
                break
            elif voto == branco:
                vBranco += 1
                vTotal += 1
                print(mensagemVoto)
                break
            else:
                print("""
=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=
Digite o número correspondente ao seu voto!
=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=""")
        elif sn[0].lower() == "n":
            print(mensagemEncerra, "\n")
            flag = False
            break
        else:
            print("""=-=-=-=-=-=-=-=-=-=-=-=-
Digite uma opção válida!
=-=-=-=-=-=-=-=-=-=-=-=-""")


percNulo = vNulo * vTotal / 100
percBranco = vBranco * vTotal / 100

print(f'''------------------
APURAÇÃO DOS VOTOS
------------------
Zé - {vZe} voto(s)
Maria - {vMaria} voto(s)
João - {vJoao} voto(s)
Tereza - {vTereza} voto(s)
Voto Nulo - {vNulo} voto(s) = {percNulo:.2f}%
Voto em Branco - {vBranco} voto(s) = {percBranco:.2f}%
''')