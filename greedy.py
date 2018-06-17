import math

class Greedy:
    def __init__(self,mat):
        self.dim=mat.getdimension()
        self.instance=mat
        self.solution=[]
        self.current=0
        self.max_color=1
        for i in range(self.dim):
            self.solution.append(1)
            
    def check_solution(self,solution,i):
        checker=[]
        supports=[]

        for k in range(i+1):
            checker.append([])
            supports.append([])
            for j in range(k+1):
                checker[k].append([])
                supports[k].append([])

        for j in range(i+1):
            if self.instance.get(i,j):
                for k in range(j,i+1):
                    c=solution[k]
                    if c not in checker[i][j]:
                        checker[i][j].append(c)
                        supports[i][j].append(c)
                    elif c in supports[i][j]:
                        supports[i][j].remove(c)


        for j in range(i+1):
            if self.instance.get(i,j) and not supports[i][j]:
                return False

        return True
    def verif(self,solution,current):
        verif_solution=[]
        for i in range(self.dim):
            verif_solution.append(1)
            
        for j in range(current):
            verif_solution[j]=1
        for j in range(current):
            if self.instance.get(current,j):
                for k in range(j,current):
                    verif_solution[k]=2
        max_color=2
        
        for i in range(current):
            c=verif_solution[i]
            while not self.check_solution(verif_solution,i+1):
                c+=1
                verif_solution[i]=c
            if c>max_color:
                max_color=c
                
        if max_color<self.max_color:
            for i in range(current):
                solution[i]=verif_solution[i]
            solution[current]=1
            self.max_color=max_color
        
    def solve(self):
        for i in range(self.dim):
            c=1
            while not self.check_solution(self.solution,i):
                c+=1
                self.solution[i]=c
            if c>self.max_color:
                self.max_color=c
                self.verif(self.solution,i)
                
    def print(self):
        for i in range(self.dim):
            print("",self.solution[i],end="")
        print()
