class DTW():
    
    def __init__(self,x,y):
        super().__init__()
        self.__x = x
        self.__y = y
        self.__matriz = []
        self.__caminho = []

        for i in range(len(self.__x)):
            self.__matriz.append([])
            for j in range(len(self.__y)):
                self.__matriz[i] += [abs(self.__x[i] - self.__y[j]) + min(self.__square(i,j))]

        self.__caminho.append((len(x)-1,len(y)-1))
        self.__busca(len(x)-1,len(y)-1)
        

    def __square(self,i,j):
        vetor = []
        if(i-1 >= 0 and j-1 >= 0):
            vetor.append(self.__matriz[i-1][j-1])
        if( i-1 >= 0 ):
            vetor.append(self.__matriz[i-1][j])    
        if( j-1 >= 0):
            vetor.append(self.__matriz[i][j-1])
        if(len(vetor) == 0 ):
            return [0]
        return vetor

    def __busca(self,i,j):
        value = min(self.__square(i,j))
        if(i-1 >= 0 and j-1 >= 0):
            if(self.__matriz[i-1][j-1] == value):
                self.__caminho.append((i-1,j-1))
                return self.__busca(i-1,j-1)
        if( i-1 >= 0 ):
            if(self.__matriz[i-1][j] == value):
                self.__caminho.append((i-1,j))
                return self.__busca(i-1,j)
        if( j-1 >= 0):
            if(self.__matriz[i][j-1] == value):
                self.__caminho.append((i,j-1))
                return self.__busca(i,j-1)

    def peso(self):
        peso = 0
        for i in self.__caminho:
            peso += self.__matriz[i[0]][i[1]]
        return peso

    

    def caminho(self):
        return self.__caminho
