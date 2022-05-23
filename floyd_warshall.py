
if __name__=='__main__':
    adj_matrix = [[1000,2,5,1,1000,1000],[2,1000,3,2,1000,1000],[5,3,1000,3,1,5],
                [1,2,3,1000,1,1000],[1000,1000,1,1,1000,1],[1000,1000,5,1000,1,1000]]
    short_paths=list(list())
    vertices=['U','V','W','X','Y','Z']
    min_val=10000
    for i in range(len(adj_matrix)):
        nest=[]
        for j in range(len(adj_matrix)):
            min_val = adj_matrix[i][j]
            if i!=j:
                for k in range(len(adj_matrix)):
                    alt=adj_matrix[i][k]+adj_matrix[k][j]
                    if alt<min_val:
                       min_val=alt

                if min_val<100:

                    nest.append(min_val)
            else:

                nest.append(0)

        short_paths.append(nest)
    print("    Shortest Paths")
    print('   U  V  W  X  Y  Z')
    for i in range(len(short_paths)):
        print(vertices[i],short_paths[i])




