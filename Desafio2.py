#Dado o grafo representado na imagem a seguir. Faça um programa que leia um arquivo contendo
# informações do grafo, gere uma matriz de adjacência e calcule o grau de cada vértice
importar  cópia
aresta  = []
classe  Aresta :
    def  __init__ ( self , n1 , n2 , peso ):
        eu . no1  =  n1
        eu . no2  =  n2
        eu . peso  =  peso

grafo  =  open ( 'arquivo.txt' , 'r' )
para  i  in  grafo :
    linha  =  i . split ()
    aresta . anexar ( Aresta ( int ( linha [ 0 ]), int ( linha [ 1 ]), int ( linha [ 2 ])))
    imprimir ( i . dividir ())
grafo . fechar ()

def  dfs ( g , não , caminho  = []):
    se  len ( caminho ) < ( len ( g ) - 1 ) e  int ( não ) >  0 :
        se  não,  não  em  path : path . anexar ( int ( não ))
        acoes  =  expandir ( g , no )
        para  ação  em  ação :
            se a  ação  não  estiver no  caminho :
                dfs ( g , acao , caminho )
                quebrar
        dfs ( g , int ( no ) - 1 , caminho )
     caminho de retorno

def  expandir ( g , não ):
    nodes  = []
    g2  =  copiar . deepcopy ( g )
    para  v  em  g2 . itens ():
        para  i  em  v :
            if  int ( no ) ==  i :
                v . remover ( int ( não ))
                nós . anexar ( v [ 0 ])
    nós . sort ()
     nós de retorno
arquivo   =  i . split ()
noEscolhido  =  input ( "Qual vértice iniciará a busca?" )

print ( 'Busca em Largura a saída é:' , dfs ( arquivo , noEscolhido ))

#print ("Busca em Largura - saída:", dfs (arquivo ['vértices'], noEscolhido))
