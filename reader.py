from dtw import DTW #Importando a classe DTW

# Lendo o arquivo
arquivo = open('aqr.txt', 'r')

teste = open('teste.txt', 'r')
testeLinha = teste.readline()
linhateste = testeLinha.split(" ")
print("Valor esperado: " + linhateste[0])
vetordeteste = list(map(float,linhateste[1:])) 

def linha(): 
  return arquivo.readline()

matrizDistancia = []
vetorResultado = []

# Faz a leitura da base de dados e vai comparando
for linha in arquivo:
  vetorResultado = [0,0]
  valoresLinha = linha.split(" ")
  # print(valoresLinha)
  # for a in valoresLinha:
  #   if(a == "\n"):
  #     valoresLinha.remove(a)

  # if(valoresLinha.__len__() >= 1):
  vetorResultado[0] = valoresLinha[0]
  vetorLinha = list(map(float,valoresLinha[1:])) 
  DTW(vetorLinha,vetordeteste).peso() #Retorna o peso do caminho 
  DTW(vetorLinha,vetordeteste).caminho() #Retorna o caminho feito

  vetorResultado[1] = (DTW(vetorLinha,vetordeteste).peso())
  matrizDistancia.append(vetorResultado)

  tuplatemp = matrizDistancia[0]
  for tupla in matrizDistancia:
    if(tupla[1] < tuplatemp[1]):
      tuplatemp = tupla

print(tuplatemp)