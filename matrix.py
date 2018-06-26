import random

class Matrix:
    def __init__(self):
        self.n = 0           # dimension
        self.m = None        # our matrix
    def createMatrixfromString(self,dim,string):
        self.n=dim
        self.m=[]
        k=0
        for i in range(self.n):
            self.m.append([])
            for j in range (i):
                self.m[i].append(0)
            self.m[i].append(1)
        for i in range(self.n):
            for j in range(i):
                self.m[i][j]=int(string[k])
                k+=1
    def createMatrix(self,dim):
        self.n = dim
        self.m = []

        for i in range(self.n):
            self.m.append([])
            for j in range(i):
                v = 0
                if random.randint(0,2) == 0:
                    v = 1
                self.m[i].append(v)
            self.m[i].append(1)

    def readMatrix(self,file):
        self.m = []
        i = -1
        with open(file) as f:
            lines = f.readlines()
            for l in lines:
                i+=1
                if len(l.strip()) == 0:
                    self.n = i
                    break
                self.m.append([])
                #print(l.strip())
                self.m[i] = [int(x) for x in l.strip(", ").split()]
                if len(self.m[i]) != i+1:
                    print("WARNING! Matrix file is corrupted.")
                #print(i,"--->",self.m[i])
        self.n = i+1
        print("n =",self.n)

    def print(self):
        for i in range(self.n):
            for j in range(i+1):
                print("",self.get(i,j),end="")
            print()

    def get(self,i,j):
        return self.m[i][j]

    def getdimension(self):
        return self.n
