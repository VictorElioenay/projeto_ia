from knn import KNN

# teste = open('teste.txt', 'r')
# arquivoTreino = 'aqr.txt'
# k = [1,3,5,10]

for n in range(5):
  print('Teste: ' + str(n))
  teste = open('./particoes/ts' + str(n) + '.txt', 'r')
  arquivoTreino = './particoes/cj' + str(n) + '.txt'
  k = [1,3,5,10]
  # testeLinha = teste.readline()
  count = 0
  accuracyDTW = 0
  accuracyEuclidiana = 0
  for testeLinha in teste:
    count += 1
    linhateste = testeLinha.split(" ")
    # print("Valor esperado: " + linhateste[0])
    vetordeteste = list(map(float,linhateste[1:])) 

    ResultadoDTW = KNN(arquivoTreino, vetordeteste, k).runKNN_DTW()
    # print(ResultadoDTW)
    ResultadoEuclidiana = KNN(arquivoTreino, vetordeteste, k).runKNN_Euclidiana()
    # print(ResultadoEuclidiana)

    hitDTW = 0 
    for i in ResultadoDTW:
      if(int(linhateste[0]) == int(i[1])):
        hitDTW += 1

    accuracyDTW += hitDTW/ResultadoDTW.__len__()

    hitEuclidiana = 0 
    for i in ResultadoEuclidiana:
      if(int(linhateste[0]) == int(i[1])):
        hitEuclidiana  += 1

    accuracyEuclidiana += hitEuclidiana/ResultadoEuclidiana.__len__()
    print("Progresso: " + str(count*100/240) + "% teste " + str(n+1))
    # print("Accuracy DTW: " + str(accuracyDTW*100/count) + "%")
    # print("Accuracy Euclidiana: " + str(accuracyEuclidiana*100/count) + "%")
  print("Accuracy DTW: " + str(accuracyDTW*100/count) + "%")
  print("Accuracy Euclidiana: " + str(accuracyEuclidiana*100/count) + "%")
