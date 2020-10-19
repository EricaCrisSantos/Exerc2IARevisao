#Dada o quebra-cabeça de 8 peças. Faça um programa que receba um estado do jogo e retorne
#todos estados subsequentes possíveis.

import timeit
import random
import copy

MATRIZ = [[1,2,3], [4,5,6],[7,8,0]]

#classe Nó em que cada nó vai quardar o endereço do nó pai para realizar a busca
class Noh:
    def init(self, estado, nopai, g, h, ): #função inicial
        self.estado = estado
        self.pai = nopai
        self.g = g
        self.h = h

    def eq(self, outro): #função para verificar se um nó é igual ao outro
        return self.estado == outro.estado

    def repr(self): #função para imprimir o valor de um nó
        return str(self.estado)

    def getState(self): #função para retornar o estado do nó
        return self.estado

#função para calcular as inversões e verificar se é solucionável ou não
def solucionavel(lista):
    inversoes = 0
    for i, e in enumerate(lista):
        if e == 0:
            continue 
        for j in range(i+1, len(lista)):
            if lista[j]==0:
                continue 
            if e > lista[j]:
                inversoes += 1
    if inversoes%2 == 1:
        return False
    else:
        return True

#Função para gerar o tabuleiro inicial
def geraInicial(st=MATRIZ[:]):
    lista = [j for i in st for j in i]
    while True:
        random.shuffle(lista)
        st = [lista[:3]]+[lista[3:6]]+[lista[6:]]
        if solucionavel(lista) and st!= MATRIZ:
            return st

#Funcao que vai licalizar um elemento qualquer no tabuleiro, por padrao encontrará o espaço em branco
def localizar(estado,elemento=0):
    for i in range(3):
        for j in range(3):
            if estado[i][j]==elemento:
                linha = i
                coluna = j
                return linha,coluna
#Dado dois estado quaisquer, Localizará a distancia quateirao total dos estados 
def distanciaQuarteirao(st1,st2):
    dist = 0
    fora = 0
    for i in range(3):
        for j in range(3):
            if st1[i][j]==0:
                continue
            i2,j2 = localizar(st2,st1[i][j])
            if i2 != i or j2 != j: fora += 1
            dist += abs(i2-i)+abs(j2-j)
    return dist + fora


def criaNo(estado,pai,g=0):
    h = g + distanciaQuarteirao(estado,MATRIZ) #heuristica A*
    return Noh(estado,pai,g,h)

#funçao para inserir nó na variavel de controle da busca
def inserirNoh(noh,fronteira):
    if noh in fronteira:
        return fronteira
    fronteira.append(noh)
    chave = fronteira[-1]
    j = len(fronteira)-2
    while fronteira[j+1].h > chave.h and j>=0:
        fronteira[j+1] = fronteira[j]
        fronteira[j] = chave
        j-=1
    return fronteira

#função dos movimentos do tabuleiro, ou seja, movendo o espaço
def moverAbaixo(estado):
    linha,coluna = localizar(estado)
    if linha < 2:
        estado[linha+1][coluna],estado[linha][coluna] = estado[linha][coluna],estado[linha+1][coluna]
    return estado

def moverAcima(estado):
    linha,coluna = localizar(estado)
    if linha > 0:
        estado[linha-1][coluna],estado[linha][coluna] = estado[linha][coluna],estado[linha-1][coluna]
    return estado

def moverDireita(estado):
    linha,coluna = localizar(estado)
    if linha < 2:
        estado[linha][coluna+1],estado[linha][coluna] = estado[linha][coluna],estado[linha][coluna+1]
    return estado

def moverEsquerda(estado):
    linha,coluna = localizar(estado)
    if linha > 0:
        estado[linha][coluna-1],estado[linha][coluna] = estado[linha][coluna],estado[linha][coluna-1]
    return estado


#retornar todos os sucessores de um nó
def succ(noh):
    estado = noh.estado
    pai = noh.pai 
    if pai:
        estadoPai = pai.estado
    else:
        estadoPai = None
    listaS = []
    l1 = moverAcima(copy.deepcopy(estado))
    if l1 != estado:
        listaS.append(l1)
    l2 = moverDireita(copy.deepcopy(estado))
    if l2 != estado:
        listaS.append(l2)
    l3 = moverAbaixo(copy.deepcopy(estado))
    if l3 != estado:
        listaS.append(l3)
    l4 = moverEsquerda(copy.deepcopy(estado))
    if l4 != estado:
        listaS.append(l4)
    return listaS


#função de busca  A*
def busca(max,nohInicio):
    print(nohInicio,":")
    nmov = 0
    borda = [nohInicio]
    while borda:
        noh = borda.pop(0)
        if noh.estado == MATRIZ:
            sol = []
            while True:
                sol.append(noh.estado)
                noh = noh.pai
                if not noh: break
            sol.reverse()
            return sol,nmov
        nmov+=1
        if (nmov%(max/10))==0: print(nmov, end="....")
        if nmov>max: break
        sucs = succ(noh)
        for s in sucs:
            inserirNoh(criaNo(s,noh,noh.g+1),borda)
    return 0,nmov


def pecas8(maxD,nAmostras):
    tempos = []
    solucionados = []
    solucoes = []
    naoSolucionados = []
    nS = 0
    nNs = 0
    for i in range(nAmostras):
        noInicial = criaNo(geraInicial(), None)
        start_time = timeit.default_timer()
        res,nmov = busca(maxD,noInicial)
        tempo = timeit.default_timer() - start_time
        if res:
            solucoes.append(tempo)
            print("\nSolucionado em {} segundos e {} movimentos ".format(tempo,nmov))
            tempos.append(tempo)
            solucionados.append((noInicial.estado,nmov))
            nS+=1
        else:
             print("\nFalhou {} segundos e {} movimentos ".format(tempo,nmov))
             naoSolucionados.append((noInicial.estado,nmov))
             tempos.append(None)
             nNs+=1
    print("\nSolucionado {} e não solucionados {} ".format(nS,nNs))
    return tempos,solucionados,naoSolucionados,nS,nNs
#geraInicial()
sol = pecas8(1,1)