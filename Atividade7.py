#6. Dado o grafo representado na imagem a seguir. Faça um programa que leia um arquivo contendo
#informações do grafo, gere uma matriz de adjacência e calcule o grau de cada vértice.

aresta = []
vertice = []
matriz = []

class Aresta:
    def init(self, n1, n2, peso):
        self.n1 = n1
        self.n2 = n2
        self.peso = peso


grafo = open('arquivo.txt', 'r')
for i in grafo:
    linha = i.split()
    aresta.append(Aresta(int(linha[0]), int(linha[1]), int(linha[2])))
grafo.close()

def inserido(vert):
    inserted = False
    for i in range( len(vertice) ):
        if (vert == vertice[i]):
            inserted = True
            break
    return inserted

for i in range( len(aresta) ): #Iterar para preencher a lista 'vertices'
    if(not inserido(aresta[i].n1)):
        vertice.append(aresta[i].n1)
    if(not inserido(aresta[i].n2)):
        vertice.append(aresta[i].n2)
vertice = sorted(vertice)

for i in range( len(vertice) ): #Preencher matriz com zeros
    linha = []
    for j in range( len(vertice) ):
        linha.append(0)
    matriz.append(linha)


for i in range( len(aresta) ): #Criando matriz adjacente
    matriz[aresta[i].n1][aresta[i].n2] = aresta[i].peso
    matriz[aresta[i].n1][aresta[i].n2] = aresta[i].peso

print() #Imprimir Matriz
print('A Matriz de Adjacencia é: ')
for i in range( len(matriz) ):
    print(matriz[i])
print()

print("O grau de cada vértice é: ") #Calculando e imprimindo o grau de cada vértice:
for i in range( len(matriz) ):
    grau = 0
    for j in range( len(matriz[i]) ):
        if(matriz[i][j] != 0):
            grau += 1
    print('Grau de {}: {}'.format(i,grau) )
