import math
import sys
from matrix import Matrix

class BruteForcer:
   def __init__(self,dim,mat):
       self.dim=dim
       self.instance=mat
       self.solution=[]
       self.best_solution=[]
       self.current=0
       self.max_color=0
       self.best_bound=math.ceil(math.log(dim,2))+1
       for i in range(dim):
          self.solution.append(0)
          self.best_solution.append(0)

   def check_solution(self):
      checker=[]
      supports=[]

      for i in range(self.current):
         checker.append([])
         supports.append([])
         for j in range(i+1):
            checker[i].append([])
            supports[i].append([])

      i=self.current-1
      for j in range(i+1):
         if self.instance.get(i,j):
            for k in range(j,self.current):
               c=self.solution[k]
               if c not in checker[i][j]:
                  checker[i][j].append(c)
                  supports[i][j].append(c)
               elif c in supports[i][j]:
                  supports[i][j].remove(c)


      for j in range(i+1):
         if self.instance.get(i,j) and not supports[i][j]:
            return False

      return True


   def solve(self):
      if not self.check_solution():
         return

      if self.current==self.dim:
         for i in range(self.dim):
            self.best_solution[i]=self.solution[i]
         self.best_bound=len(set(self.solution))
         print("Found: ",end="")
         self.print()
         print("> New bound to beat:",self.best_bound)
         return

      for c in range(1,self.best_bound+1):
         self.solution[self.current]=c
         self.current+=1
         old_max=self.max_color
         if c>self.max_color:
            self.max_color=c

         if self.max_color<self.best_bound:
            self.solve()

         self.max_color=old_max
         self.current-=1

         if c>=self.best_bound:
            break

   def print_current(self):
      for i in range(self.dim):
         print("",self.solution[i],end="")
      print()
   def print(self):
      for i in range(self.dim):
         print("",self.best_solution[i],end="")
      print()

if __name__ == "__main__":
    dim=20
    if len(sys.argv)>1:
        dim = int(sys.argv[1])
    m = Matrix()
    m.createMatrix(dim)
    s=BruteForcer(dim,m)
    m.print()
    s.solve()
    print("Best found: ",end="")
    s.print()
