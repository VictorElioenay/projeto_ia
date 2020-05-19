from dtw import DTW #Importando a classe DTW
from euclidiana import Euclidiana

class Reader:
  def __init__(self, nomeCjTreino, vetordeteste):
    self.arquivo = open(nomeCjTreino, 'r')
    self.vetordeteste = vetordeteste

  def RunDTW(self):
    # Lendo o arquivo
    # testeLinha = self.teste.readline()
    # linhateste = testeLinha.split(" ")
    # vetordeteste = list(map(float,linhateste[1:])) 

    matrizDistancia = []
    vetorResultado = []

    # Faz a leitura da base de dados e vai comparando
    # count=0
    for linha in self.arquivo:
      # count += 1
      vetorResultado = [0,0,0]
      valoresLinha = linha.split(" ")
      vetorResultado[0] = valoresLinha[0]
      vetorLinha = list(map(float,valoresLinha[1:])) 
      vetorResultado[1] = DTW(vetorLinha,self.vetordeteste).peso()
      matrizDistancia.append(vetorResultado)
    # print(count)
    return matrizDistancia

  def RunEuclidiana(self):
    # Lendo o arquivo
    # testeLinha = self.teste.readline()
    # linhateste = testeLinha.split(" ")
    # vetordeteste = list(map(float,linhateste[1:])) 


    matrizDistancia = []
    vetorResultado = []

    # Faz a leitura da base de dados e vai comparando
    for linha in self.arquivo:
      vetorResultado = [0,0]
      valoresLinha = linha.split(" ")
      vetorResultado[0] = valoresLinha[0]
      vetorLinha = list(map(float,valoresLinha[1:])) 
      vetorResultado[1] = Euclidiana(vetorLinha,self.vetordeteste).peso() #Retorna o peso do caminho 
      matrizDistancia.append(vetorResultado)

    return matrizDistancia

# Site para o counter
#https://www.it-swarm.dev/pt/python/maneira-mais-rapida-de-contar-o-numero-de-ocorrencias-em-uma-lista-do-python/1069664102/