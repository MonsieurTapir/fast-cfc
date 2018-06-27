import math
import sys
from matrix import Matrix
from greedy import Greedy
from dynamic import DynamicProgramming
class BruteForcer:
    def __init__(self,mat):
        self.dim=mat.getdimension()
        self.instance=mat
        self.solution=[]
        self.best_solution=[]
        self.current=0
        self.max_color=0
        self.best_bound=math.ceil(math.log(self.dim,2))+1
        for i in range(self.dim):
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
            # print("Found: ",end="")
            #self.print()
            #print("> New bound to beat:",self.best_bound)
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
    def get_best(self):
        return self.best_bound 
    def print_current(self):
        for i in range(self.dim):
            print("",self.solution[i],end="")
        print()
    def print(self):
        for i in range(self.dim):
            print("",self.best_solution[i],end="")
        print()


def test_all_instances(dim):
    size=(dim*(dim-1))/2
    total=int(math.pow(2,size))
    toolow=0
    toohigh=0
    
    formatter='0'+str(int(size))+'b'
    fileout=open("n="+str(dim),"w")
    for i in range(int(math.pow(2,size))):
        m=Matrix()
        m.createMatrixfromString(dim,format(i,formatter))
        s=BruteForcer(m)
        s.solve()
        lb=DynamicProgramming(m,0).compute(0,dim-1)
        ub=DynamicProgramming(m,1).compute(0,dim-1)
        g=Greedy(m)
        g.solve()
        if lb!=s.get_best():
            toolow+=1
        if ub!=s.get_best():
            toohigh+=1
        fileout.write(str(s.get_best())+";"+str(lb)+";"+str(ub)+";"+str(g.get_opt_val())+"\n")
    fileout.close()
        
    print("Total instances:",total)
    print("Too low:",toolow)
    print("Too high:",toohigh)
if __name__ == "__main__":
    m = Matrix()
    
    dim=5
    if len(sys.argv)>1:
        dim = int(sys.argv[1])
    if dim <= 0:
        m.readMatrix(sys.argv[2])
        dim = m.getdimension()
    else:
        m.createMatrix(dim)
    s = BruteForcer(m)
    s.solve()
    s.print()
    #k=0
    #test_all_instances(dim)
    '''
    while 1:
        m=Matrix()
        m.createMatrix(dim)
        s=BruteForcer(m)
        s.solve()
        lb=DynamicProgramming(m,0).compute(0,dim-1)
        ub=DynamicProgramming(m,1).compute(0,dim-1)
        if lb != s.get_best():
            m.print()
            s.print()
            print("OPT: ",s.get_best())
            print("Dyn LB: ",lb)
            print("Dyn UB: ",ub)
            break
        k+=1
    print("Tried : ",k," instances")
    '''
          
     #s=BruteForcer(m)
     #g=DynamicProgramming(m)
     #m.print()
     #s.solve()
     #print("Best found: ",end="")
     #s.print()
     #print("======================")
     #print("DP found: ",g.compute(0,m.getdimension()-1))
