from dtw import DTW #Importando a classe DTW

# Lendo o arquivo
arquivo = open('aqr.txt', 'r')

def linha(): 
  return arquivo.readline()

matrizDistancia = []
vetorResultado = []

for linha in arquivo:
  valoresLinha = linha.split(" ")
  vetorResultado.append(valoresLinha[0])
  vetorLinha = list(map(float,valoresLinha[1:])) 
  DTW(vetorLinha,vetordeteste).peso() #Retorna o peso do caminho 
  DTW(vetorLinha,vetordeteste).caminho() #Retorna o caminho feito

  # vetorResultado.append(dtw(vetorLinha, vetordeteste))
  # matrizDistancia.append(vetorResultado)

# index = matrizDistancia.index(min(matrizDistancia))
# print(matrizDistancia[index,0])