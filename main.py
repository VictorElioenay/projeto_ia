from knn import KNN

teste = open('teste.txt', 'r')
testeLinha = teste.readline()
linhateste = testeLinha.split(" ")
print("Valor esperado: " + linhateste[0])
vetordeteste = list(map(float,linhateste[1:])) 

# ResultadoObtido = KNN('aqr.txt', 'teste.txt').runKNN_DTW()
# print(ResultadoObtido)

ResultadoObtido2 = KNN('aqr.txt', 'teste.txt').runKNN_Euclidiana()
print(ResultadoObtido2)