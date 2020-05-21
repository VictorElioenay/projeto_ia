from knn import KNN
from threading import Thread

def main(n):
  print('Teste: ' + str(n))
  teste = open('./particoes/ts' + str(n) + '.txt', 'r')
  arquivoTreino = './particoes/cj' + str(n) + '.txt'
  k = [1,3,5,10]
 
  count = 0
  hitDTW = [0,0,0,0]
  hitEuclidiana = [0,0,0,0]
  for testeLinha in teste:
    count += 1 #Conta quantas linhas ja foram executadas
    linhateste = testeLinha.split(" ")
    vetordeteste = list(map(float,linhateste[1:])) 

    ResultadoDTW = KNN(arquivoTreino, vetordeteste, k).runKNN_DTW()
    ResultadoEuclidiana = KNN(arquivoTreino, vetordeteste, k).runKNN_Euclidiana()

  #Contador de acertos:
    pos = 0
    for i in ResultadoDTW:
      if(int(linhateste[0]) == int(i[1])):
        hitDTW[pos] += 1
      pos += 1

    pos = 0
    for i in ResultadoEuclidiana:
      if(int(linhateste[0]) == int(i[1])):
        hitEuclidiana[pos] += 1
      pos += 1

    print("Progresso" + str(n) + ": " + str(count*100/240) + "%")
  
  #Relatorio dos testes:
  relatorio = open("./relatorios/relatorioFinal"+ str(n) + ".txt", "w")
  relatorio.write('Teste: ' + str(n) + "\n")
  relatorio.write("Accuracy DTW K=1: " + str(hitDTW[0]*100/count) + "% \n")
  relatorio.write("Accuracy DTW K=3: " + str(hitDTW[1]*100/count) + "% \n")
  relatorio.write("Accuracy DTW K=5: " + str(hitDTW[2]*100/count) + "% \n")
  relatorio.write("Accuracy DTW K=10: " + str(hitDTW[3]*100/count) + "% \n")
  relatorio.write("Accuracy DTW TOTAL: " +  str(((hitDTW[0] + hitDTW[1] + hitDTW[2] + hitDTW[3])*100)/(4*count)) + "% \n")
  relatorio.write("Accuracy Euclidiana K=1: " + str(hitEuclidiana[0]*100/count) + "% \n")
  relatorio.write("Accuracy Euclidiana K=3: " + str(hitEuclidiana[1]*100/count) + "% \n")
  relatorio.write("Accuracy Euclidiana K=5: " + str(hitEuclidiana[2]*100/count) + "% \n")
  relatorio.write("Accuracy Euclidiana K=10: " + str(hitEuclidiana[3]*100/count) + "% \n")
  relatorio.write("Accuracy Euclidiana TOTAL: " + str(((hitEuclidiana[0] + hitEuclidiana[1] + hitEuclidiana[2] + hitEuclidiana[3])*100)/(4*count)) + "% \n")


class Th(Thread):

  def __init__ (self, num):
    Thread.__init__(self)
    self.num = num

  def run(self):
    main(self.num)

a = Th(0)
a.start() 
a = Th(1)
a.start() 
a = Th(2)
a.start() 
a = Th(3)
a.start() 
a = Th(4)
a.start() 
