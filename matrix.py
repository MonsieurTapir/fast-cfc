import random

class Matrix:

   def __init__(self):
      self.n = 0       # dimension
      self.m = None    # our matrix

   def createMatrix(self,dim):
      self.n = dim
      self.m = []

      for i in range(self.n):
         self.m.append([])
         for j in range(i):
            v = 0
            if random.randint(0,5) == 0:
               v = 1
            self.m[i].append(v)
         self.m[i].append(1)


   def print(self):
      for i in range(self.n):
         for j in range(i+1):
            print("",self.get(i,j),end="")
         print()

   def get(self,i,j):
      return self.m[i][j]

   def getdimension(self):
      return self.n
