import math

class DynamicProgramming:
    def __init__(self,mat,offset):
        self.dim=mat.getdimension()
        self.instance=mat
        self.table=[]
        self.offset=offset
        for i in range(self.dim):
            self.table.append([])
            for j in range (self.dim):
                self.table[i].append(-1)
                if i==j:
                    self.table[i][j]=1
                if (i+1)==(j):
                    if self.instance.get(j,i):
                        self.table[i][j]=2
                    else:
                        self.table[i][j]=1
                if i==(j+1):
                    if self.instance.get(i,j):
                        self.table[i][j]=2
                    else:
                        self.table[i][j]=1

    def compute(self,i,j):
       # print("computing [",i,"][",j,"]",self.table[i][j])
        if self.table[i][j]!=-1:
            return self.table[i][j]

        min_T=self.dim
        max_T=0
        for k in range(i,j+1):
            T1=1
            T2=1
            if k-1>=i:
                T1=self.compute(i,k-1)
            if k+1<=j:
                T2=self.compute(k+1,j)
            T=max(T1,T2)
            if T>max_T:
                max_T=T
            if T<min_T:
                min_T=T
        if min_T<max_T:
            self.table[i][j]=max_T
        
        elif self.instance.get(j,i):
            self.table[i][j]=max_T+1
        else:
            if i<j-1 and self.compute(i+1,j-1)<max_T:
                self.table[i][j]=max_T
            else:
                self.table[i][j]=max_T+self.offset
        return self.table[i][j]

    
            
