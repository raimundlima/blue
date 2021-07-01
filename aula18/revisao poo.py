# # class Pessoa:
# #     def crescer(self):
# #         print('eu cresci')


# # pessoa=Pessoa()
# # pessoa.crescer

# class Conta:
#     def __init__(self,titular,saldo):
#         self.titular = titular
#         self.conta = saldo

# cliente1 = Conta('Eu',50000)

# class Funcionário:
#     def __init__ (self,nome,cargo,valor_hora_trabalhada):
#         self.nome = nome
#         self.cargo = cargo,
#         self.valor_hora_trabalhada = valor_hora_trabalhada
#         self.__salario = 0
#         self.__horas_trabalhadas = 0
        

# @property
# def salario(self):
#     return self.__salario

# @salario.setter
# def salario(self, novo_salario):
#     raise ValueError("Impossivel alterar salario diretamente. Use a função calcula_salario().")

# def registra_hora_trabalhada(self):
#     self.__horas_trabalhadas += 1

# def calcula_salario(self):
#     self.__salario=self.__horas_trabalhadas * self.valor_hora_trabalhada

# pedro = Funcionário ("Pedro" ,"Gerente de vendas", 500)
# print(vars(pedro))


class BombaCombustivel:
    def __init__ (self,tipoCombustivel, valorLitro, quantidadeLitro,quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
        self.quantidadeLitro = quantidadeLitro  

    def abastecerPorFavor (self):
        self.quantidadeCombustivel * self.valorLitro
        

    def abastecerPorLitro (self):
        self.quantidadeLitro * self.valorLitro

    def alterarValor (self):
        self.valorLitro

    def alterarCombustivel (self):
        self.tipoCombustivel

    def alterarQuantidadeCombustivel(self):
        self.quantidadeCombustivel


