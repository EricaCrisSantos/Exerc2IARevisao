#Dado o grafo representado na imagem a seguir. Faça um programa que leia um arquivo contendo
#informações do grafo, gere uma matriz de adjacência e calcule o grau de cada vértice

import copy
aresta = []
vertice = {}

class Aresta: 
    def __init__(self, n1, n2, peso):
        self.n1 = n1
        self.n2 = n2
        self.peso = peso


grafo = open('arquivo.txt', 'r')
for i in grafo:
    linha = i.split()
    aresta.append(Aresta(int(linha[0]), int(linha[1]), int(linha[2])))
    print(i.split())
grafo.close()
def bfs(g, no):
    fila = []
    path = []
    while len(path) < (len(g) - 1):
        if no not in path:
            path = path+[int(no)]
            acoes = expandir(g,no)
        #acoes = expandir(g,no)
        for acao in acoes:
            if acao not in path:
                path = path+[acao]
                fila = fila+[acao]
        fila.sort()
        fila.reverse()
        no = fila.pop()
    return path

def expandir(g, no):
    nodes = []
    g2 = copy.deepcopy(g)
    for n,v in g2.items():
        for i in v:
            if int(no) == i:
                v.remove(int(no))
                nodes.append(v[0])
    nodes.sort()
    return nodes

arquivo  = i.split()

noEscolhido = input("Qual vértice iniciará a busca: ")

print('Busca em Largura a saída é: ', bfs(arquivo, noEscolhido))

