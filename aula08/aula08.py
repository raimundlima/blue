#l = [10,20,30,40,50]
#print(l[3:])
#print(l[1:3])



# l2 = [10,20,30,40,50,60]
# #print(l2)
# #print(type(l2))
# l2[3] = "pizza"
# print(l2)
# #for indice_atual in range(len(l2)):
# #    l2[indice_atual] = input('digite novo valor')
# print(l2)
# l2.append("joint")
# print(l2)

#lista vazia:
# lvazia = []
# for i in range(5):
#     lvazia.append(input('Digite um valor: \n'))
#     if i not in lvazia:
#         lvazia.append(i)
#     elif i in lvazia:
#         print('Duplicate')
    
# print(lvazia)

# numeros = list()
# while True:
#     pergunta=int(input('Digite um Valor: '))
#     if pergunta not in numeros:
#         numeros.append(pergunta)
#         print('Numero Adcionado!')    
    
#     else:
#         print('Valor Duplicado, Digite outro')


#     resposta= input('Deseja imprimir os numeros ou quer continuar? [I/C]: ')
#     for i in resposta:
#         if i not in 'IiCc':
#             resposta= input('Deseja imprimir os numeros ou quer continuar? [I/C]: ')
#     if resposta in 'Ii':
#          break
# print(numeros)


lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um número: (0 para sair) ')))
    if lista == 0:
        lista.pop()
        break

    if lista % 2 == 0:
        par.append(lista)
    else:

        impar.append(lista)

#print(f'''Lista: {lista}
#Par: {par}
#Impar: {impar}''')
print(f'par{par}')


