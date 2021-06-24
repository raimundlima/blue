from datetime import date

# ano = date.today().year
# jovem = 0
# adulto = 0
# atual = 0
# #counter_young = 0
# #counter_adult = 0
    
# for n in atual:
#         num = int(input("Digite anos de nascimento: \n"))
# if ano - num >= 18:
#         print('pode votar')
# elif atual - num <= 16:
#         print('não pode votar')


# idade = int(input('qual é a sua idade ? \n'))
# if idade >= 18:
#         print('Maior de idade')
#         elif idade <16 :
#         print ('menor de idade')


atual = date.today().year
def check_age (idade):
    
    idade = atual - nas
    if idade > 18:
            print('seu voto é obrigatório')
    elif idade >= 16 and idade <= 17:
            print ('seu voto é opcional')
    else:
            print ('voce não pode votar ')

nas = int(input('Por favor insira sua data de nascimento \n'))
check_age(atual-nas)

