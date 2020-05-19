from collections import Counter
from reader import Reader

class KNN:
  def __init__(self, nomeCjTreino, vetordeteste, k):
    self.nomeCjTreino = nomeCjTreino
    self.vetordeteste = vetordeteste
    self.k = k

  def runKNN_DTW(self):
    reader = Reader(self.nomeCjTreino, self.vetordeteste)

    #Gasta muito processameto então o ideal é aproveitar os dados
    matrizDTW = reader.RunDTW()  
    
    matrizDTW.sort(key=lambda tup: tup[1])
    ocorrencias = []

    resultado = []

    for i in range(self.k.__len__()):
      resultadotemp = []
      for x in range(self.k[i]):
        ocorrencias.append(matrizDTW[x][0])
      c = Counter(ocorrencias).most_common()
      # resultadotemp.append("K = " + str(k[i]))
      resultadotemp.append(self.k[i])
      resultadotemp.append(c[0][0])
      resultado.append(resultadotemp)

    # Retorna a ocorrencia mais comum
    return resultado

  def runKNN_Euclidiana(self):
    reader = Reader(self.nomeCjTreino, self.vetordeteste)

    matrizEuclidiana = reader.RunEuclidiana()  

    matrizEuclidiana.sort(key=lambda tup: tup[1])
    ocorrencias = []

    resultado = []

    for i in range(self.k.__len__()):
      resultadotemp = []
      for x in range(self.k[i]):
        ocorrencias.append(matrizEuclidiana[x][0])
      c = Counter(ocorrencias).most_common()
      # resultadotemp.append("K = " + str(k[i]))
      resultadotemp.append(self.k[i])
      resultadotemp.append(c[0][0])
      resultado.append(resultadotemp)
    
    return resultado
    

