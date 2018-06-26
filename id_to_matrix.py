import sys
if __name__ == "__main__":
    if len(sys.argv)<3:
        print("First argument: dimension")
        print("Second argument: instance id")
        exit(1)
    dim=int(sys.argv[1])
    inst=int(sys.argv[2])
    size=(dim*(dim-1))/2
    formatter='0'+str(int(size))+'b'
    mat_string=format(inst,formatter)
    k=0
    for i in range(dim):
        for j in range(i):
            print(mat_string[k],end=" ")
            k+=1
        print("1")
