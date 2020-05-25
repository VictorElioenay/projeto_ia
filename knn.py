from collections import Counter
from reader import Reader

class KNN:
  def __init__(self, nomeCjTreino, vetordeteste, k):
    self.nomeCjTreino = nomeCjTreino
    self.vetordeteste = vetordeteste
    self.k = k

  def runKNN_DTW(self):
    #Carrega o reader com os valores do conjunto de treino e a linha a ser testada
    reader = Reader(self.nomeCjTreino, self.vetordeteste)
    matrizDTW = reader.RunDTW()  
    
    #Ordena a matriz de ditancias entre o teste e o conjunto de treino em orgem crescente
    matrizDTW.sort(key=lambda tup: tup[1])
    ocorrencias = []

    resultado = []

    #Itera no vetor de valores de k (assim o programa não precisa recalcular pra cada valor de k, ja faz tudo de uma vez)
    for i in range(self.k.__len__()):
      resultadotemp = []
      #Pega os K vizinhos mais proximos e vê qual ocorre mais vezes
      for x in range(self.k[i]):
        ocorrencias.append(matrizDTW[x][0])
      c = Counter(ocorrencias).most_common()
      resultadotemp.append(self.k[i])
      resultadotemp.append(c[0][0])
      resultado.append(resultadotemp)

    # Retorna a ocorrencia mais comum
    return resultado

  def runKNN_Euclidiana(self):
    #Carrega o reader com os valores do conjunto de treino e a linha a ser testada
    reader = Reader(self.nomeCjTreino, self.vetordeteste)
    matrizEuclidiana = reader.RunEuclidiana()  

    #Ordena a matriz de ditancias entre o teste e o conjunto de treino em orgem crescente
    matrizEuclidiana.sort(key=lambda tup: tup[1])
    ocorrencias = []

    resultado = []

    #Itera no vetor de valores de k (assim o programa não precisa recalcular pra cada valor de k, ja faz tudo de uma vez)
    for i in range(self.k.__len__()):
      resultadotemp = []
      #Pega os K vizinhos mais proximos e vê qual ocorre mais vezes
      for x in range(self.k[i]):
        ocorrencias.append(matrizEuclidiana[x][0])
      c = Counter(ocorrencias).most_common()
      resultadotemp.append(self.k[i])
      resultadotemp.append(c[0][0])
      resultado.append(resultadotemp)
    
    return resultado
    

