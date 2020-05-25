from dtw import DTW #Importando a classe DTW
from euclidiana import Euclidiana

class Reader:
  #C arrega o reader com o conjunto de treino e o vetor a ser testado(vetor é a linha de testes transformada em floats)
  def __init__(self, nomeCjTreino, vetordeteste):
    self.arquivo = open(nomeCjTreino, 'r')
    self.vetordeteste = vetordeteste

  def RunDTW(self):
    matrizDistancia = []
    vetorResultado = []

    # Faz a leitura da base de dados e vai comparando
    for linha in self.arquivo:
      vetorResultado = [0,0,0]
      valoresLinha = linha.split(" ")
      vetorResultado[0] = valoresLinha[0]
      vetorLinha = list(map(float,valoresLinha[1:])) 
      vetorResultado[1] = DTW(vetorLinha,self.vetordeteste).peso() #Retorna o peso do caminho 
      matrizDistancia.append(vetorResultado)

    return matrizDistancia

  def RunEuclidiana(self):
    matrizDistancia = []
    vetorResultado = []

    # Faz a leitura da base de dados e vai comparando
    for linha in self.arquivo:
      vetorResultado = [0,0]
      valoresLinha = linha.split(" ")
      vetorResultado[0] = valoresLinha[0]
      vetorLinha = list(map(float,valoresLinha[1:])) 
      vetorResultado[1] = Euclidiana(vetorLinha,self.vetordeteste).peso() #Retorna a distancia entre os vetores
      matrizDistancia.append(vetorResultado)

    return matrizDistancia