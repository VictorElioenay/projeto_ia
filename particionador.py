#Criador de arquivos para validação cruzada
for n in range(5):
  entrada = open('aqr.txt', 'r')
  count = 0
  conjTreino = open('./particoes/cj' + str(n) + '.txt', 'w')
  conjTeste = open('./particoes/ts' + str(n) + '.txt', 'w')
  for linhaEntrada in entrada:
    count += 1
    if( (20*n) < count < (20*(n+1) + 1) ):
      conjTeste.write(linhaEntrada)
    else:
      conjTreino.write(linhaEntrada)
      if(count == 101):
        count = 0
  
