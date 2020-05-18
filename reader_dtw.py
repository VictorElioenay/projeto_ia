from dtw import DTW #Importando a classe DTW

class Reader:
  def __init__(self, nomeCjTreino, nomeCjTeste):
    self.arquivo = open(nomeCjTreino, 'r')
    self.teste = open(nomeCjTeste, 'r')

  def RunDTW(self):
    # Lendo o arquivo
    testeLinha = self.teste.readline()
    linhateste = testeLinha.split(" ")
    # print("Valor esperado: " + linhateste[0])
    vetordeteste = list(map(float,linhateste[1:])) 

    def linha(self): 
      return self.arquivo.readline()

    matrizDistancia = []
    vetorResultado = []

    # Faz a leitura da base de dados e vai comparando
    for linha in self.arquivo:
      vetorResultado = [0,0]
      valoresLinha = linha.split(" ")
      vetorResultado[0] = valoresLinha[0]
      vetorLinha = list(map(float,valoresLinha[1:])) 
      DTW(vetorLinha,vetordeteste).peso() #Retorna o peso do caminho 
      DTW(vetorLinha,vetordeteste).caminho() #Retorna o caminho feito

      vetorResultado[1] = (DTW(vetorLinha,vetordeteste).peso())
      matrizDistancia.append(vetorResultado)

    return matrizDistancia

# Site para o counter
#https://www.it-swarm.dev/pt/python/maneira-mais-rapida-de-contar-o-numero-de-ocorrencias-em-uma-lista-do-python/1069664102/

#   tuplatemp = matrizDistancia[0]
#   for tupla in matrizDistancia:
#     if(tupla[1] < tuplatemp[1]):
#       tuplatemp = tupla

# print(tuplatemp)