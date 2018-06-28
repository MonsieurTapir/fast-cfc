from matrix import Matrix
import sys
import networkx as nx
import matplotlib.pyplot as plt
import math
import itertools

def createMatchingGraph(m):
    g = nx.Graph()
    n = m.getdimension()                    # 'left' vertices
    k = math.ceil(math.log(n,2))+1   # upper bound
    # first, the vertex nodes
    vs = [str(i) for i in range(n)]
    g.add_nodes_from(vs)
    # then the color nodes
    for v in vs:
        # the default color
        g.add_node(v+"_d")
        g.add_edge(v,v+"_d",weight=0.1)
        v_k_pair = [(str(v)+"_"+str(i), int(i+1)) for i in range(k+1)]
        print(v_k_pair)
        g.add_nodes_from([a for (a,b) in v_k_pair])
        # with weighted edges
        for u in v_k_pair:
            g.add_edge(v,u[0],weight=u[1])

    # and now we add the edges of the cliques, with large weight!
    # The cliques contains all the color vertices of the vertices inside a given intervalself.
    # We create odd cliques, hence a matching must cover a vertex (sharing an edge with a color verte)
    # in each clique; this is our support.

    # OLD VERSION
    for i in range(n):
        for j in range(i):
            if m.get(i,j) >= 1:
                # for c in range(k):
                tset = set()
                print("(",i,"-",j," + 1) x",k,"=",(i-j+1)*k)
                if ((i-j+1)*k % 2 == 0):
                    x = "x"+str(j)+"_"+str(i)
                    g.add_node(x)
                    tset = itertools.permutations(itertools.chain([x],[str(a)+"_"+str(b) for (a,b) in itertools.product(range(j,i+1),range(k+1))]),2)
                else:
                    tset = itertools.permutations([str(str(a)+"_"+str(b)) for a,b in itertools.product(range(j,i+1),range(k+1))],2)
                for t in tset:
                    # print1(t)
                    if t[0] == t[1]:
                        continue
                    g.add_edge(t[0],t[1],weight=(n+k+2)^2)

    # NEW VERSION
    # for i in range(n):
    #     for j in range(i+1):
    #         if m.get(i,j) >= 1:
    #             for t in itertools.product(itertools.combinations(range(j,i+1),2), itertools.combinations(range(k),2)):
    #                 pass

    matching = sorted([ sorted(x) for x in nx.max_weight_matching(g)])
    for v1,v2 in matching:
        if v1.isdigit():
            print(v1,"color:",v2[-1])
        elif v2.isdigit():
            print(v2,"color:",v1[-1])

    print("Maximum weight matching:",matching)
    # print("edges:",g.edges())
    # print("weights",nx.get_edge_attributes(g,'weight'))
    nx.draw_networkx(g,with_labels=True)
    plt.show()
    return g

if __name__ == "__main__":
    print("Welcome the Caperture Labs!")
    m  = Matrix()
    if len(sys.argv)>1:
        # print(len(sys.argv))
        if sys.argv[1].isdigit():
            # dimension of the random Matrix
            print("Creating random matrix")
            m.createMatrix(int(sys.argv[1]))
        else:
            # filename given in parameter
            print("Reading matrix from file")
            m.readMatrix(sys.argv[1])
    m.print()
    g = createMatchingGraph(m)
