from collections import Counter
from reader_dtw import Reader

class KNN:
  def __init__(self, nomeCjTreino, nomeCjTeste):
    self.nomeCjTreino = nomeCjTreino
    self.nomeCjTeste = nomeCjTeste

  def runKNN_DTW(self, k):
    reader = Reader(self.nomeCjTreino, self.nomeCjTeste)

    matrizDTW = reader.RunDTW()

    matrizDTW.sort(key=lambda tup: tup[1])
    ocorrencias = []

    for x in range(k):
      ocorrencias.append(matrizDTW[x][0])
    c = Counter(ocorrencias).most_common()
    
    # Retorna a ocorrencia mais comum
    return c[0][0]