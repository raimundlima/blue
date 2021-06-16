#resp = int (input('Escolha um numero para gerar a tabua: '))


menor = 10000
maior = 0

for p in range(5):
    peso = float(input('Qual o seu peso \n'))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print ('O maior peso foi', maior)
print ('O menor peso foi',menor )