from math import sqrt

class Euclidiana:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # Retorna o peso (a distancia total entre os dois vetores)
  def peso(self):
    dist = 0
    if(self.x.__len__() > self.y.__len__()):
      for i in range(self.x.__len__()):
          try:
            dist += (self.x[i] - self.y[i])**2 
          except:
            pass

    else:
      for i in range(self.y.__len__()):
        try:
          dist += (self.x[i] - self.y[i])**2 
        except:
          pass

    return sqrt(dist)
