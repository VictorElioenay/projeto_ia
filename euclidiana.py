from math import sqrt

class Euclidiana:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def peso(self):
    dist = 0
    if(self.x.__len__() > self.y.__len__()):
      for i in range(self.x.__len__()):
          try:
            dist += sqrt(self.x[i]**2 + self.y[i]**2)
          except:
            dist += sqrt(self.x[i]**2)

      dist = dist/self.x.__len__()
    else:
      for i in range(self.y.__len__()):
        try:
          dist += sqrt(self.x[i]**2 + self.y[i]**2)
        except:
          dist += sqrt(self.y[i]**2)

      dist = dist/self.y.__len__()
    return dist
