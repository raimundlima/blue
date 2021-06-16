#Caixa eletrônico
#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
#O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

#quantidade_n1 = 1
#quantidade_n2 = 5
#quantidade_n3 = 10
#quantidade_n4 = 50
#quantidade_n5 = 100


quantidade_n1 = 0
quantidade_n2 = 0
quantidade_n3 = 0
quantidade_n4 = 0
quantidade_n5 = 0

valor_n1 = 1
valor_n2 = 5
valor_n3 = 10
valor_n4 = 50
valor_n5 = 100

Valor_Minimo = 10 
Valor_Maximo = 600

quantidade_sacar = float(input('Qual a quantidade que voce quer sacar?'))

while quantidade_sacar < Valor_Minimo or quantidade_sacar > Valor_Maximo:
    print(f'O valor informado não é permitida. Favor informar um valor entre {Valor_Minimo} e  {Valor_Maximo} R$ \n')
    
quantidade_auxiliar = quantidade_sacar

quantidade_n5 = int(quantidade_n5//100)
quantidade_auxiliar = quantidade_auxiliar - (quantidade_n5*valor_n5)

quantidade_n4 = int(quantidade_n4//50)
quantidade_auxiliar = quantidade_auxiliar - (quantidade_n4*valor_n4)

quantidade_n3 = int(quantidade_n3//10)
quantidade_auxiliar = quantidade_auxiliar - (quantidade_n3*valor_n3)

quantidade_n2 = int(quantidade_n2//5)
quantidade_auxiliar = quantidade_auxiliar - (quantidade_n2*valor_n2)

quantidade_n1 = int(quantidade_n1//1)

print(f'para sacar{quantidade_sacar} reais vc precisa de: \n')
print(f'{quantidade_n5} notas de 100' )
print(f'{quantidade_n4} notas de 50')
print(f'{quantidade_n3} notas de 10 ')
print(f'{quantidade_n2} notas de 5 ')
print(f'{quantidade_n1} notas de 1 ')
