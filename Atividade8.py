#Usando recursividade, faça um programa que 
# calcule a soma dos valores de um vetor.
tv = int(input('Digite o tamanho do vetor:'))
print(tv)

vetor=[]
for i in range (0,tv): 
    vetor.append(int(input('Digite um número:')))
print(vetor)


def soma_vetor(vetor):
    if len(vetor) == 1:
        return vetor[0]
    else:
        return vetor[0] + soma_vetor(vetor[1:])
 
print("A soma do vetor é: ", soma_vetor(vetor))