# valorlista = []
# while True:
#     n = int(input('Entre o seu valor: '))

#     if n not in valorlista:
#         valorlista.append(n)
#     else:
#         print('Numero Duplicado')
#     sair = str(input('Voce quer continuar? [s/n] \n')).upper()

#     if sair == 'N' : 
#         break

# print('-' * 30)
#valorlista.sort()
#print(valorlista)

# valuesList = []
# while True:
#     n = int(input('Enter with value: '))

#     if n not in valuesList:
#         valuesList.append(n)
#     else:
#         print('Duplicate')
#     leave = str(input('Do you want leave? [y/n] ')).upper()

#     if leave in 'Y':
#         break

# print('-' * 30)
# #valuesList.sort()
# print(valuesList)


from random import randint



# jogos= 2
# l= list()

# for i in range (jogos):
#     for i in range (6):
#         n=randint(0,60)
        
#         if n not in l:
#             l.append(n) 

# print (l)


# rom random import randint



jogos= 2
cont=0
l= list()




while cont != jogos:
    for i in range (6):
        n=randint(0,60)
        
        if n not in l:
            l.append(n) 

#print (l)
print(len(l))



