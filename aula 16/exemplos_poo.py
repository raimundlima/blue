# class Mamifero ():
#     def __init__(self,nome,pelo,cor, tamanho,idade):
#         self.nome = nome
#         self.pelo = pelo
#         self.cor = cor
#         self.tamanho = tamanho
#         self.idade = idade


#     def crescer(self):
#         self.idade +=1
    
#     def locomover(self):
#         print('ele esta andando')

#     # def comer():

# cachorro = Mamifero ("Odin","curto","branco","grande", 4)
# #print (type(cachorro))
# print (vars(cachorro))



class pessoa():
    def __init__(self,nome,sobrenome,idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def dados(self):
        print(f'Nome Completo:{self.nome} {self.sobrenome}\nIdade: {self.idade}') 
gustavo = pessoa ('Gustavo', 'Batata', 27)
gustavo.dados()

