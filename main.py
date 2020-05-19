from knn import KNN

teste = open('teste.txt', 'r')
arquivoTreino = 'aqr.txt'

# testeLinha = teste.readline()
for testeLinha in teste:
  linhateste = testeLinha.split(" ")
  print("Valor esperado: " + linhateste[0])
  vetordeteste = list(map(float,linhateste[1:])) 
  ResultadoObtido = KNN(arquivoTreino, vetordeteste).runKNN_DTW()
  print(ResultadoObtido)

  ResultadoObtido2 = KNN(arquivoTreino, vetordeteste).runKNN_Euclidiana()
  print(ResultadoObtido2)
