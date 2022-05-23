class Graph:
    def __init__(self, Nodes):
        self.nodes = Nodes
        self.adj_list = {}
        for node in self.nodes:
            self.adj_list[node] = []

    def print_adj_List(self):
        for node in self.nodes:
            print(node, "-->", self.adj_list[node])

    def add_edge(self, x, y, weight):

        if y not in self.adj_list[x]:
            self.adj_list[x].append((y, weight))

        if x not in self.adj_list[y]:
            self.adj_list[y].append((x, weight))

    def depth_first_search(self, vertex, visited):
        visited.append(vertex)
        for j in self.adj_list[vertex]:
            if j[0] not in visited:
                self.depth_first_search(j[0], visited)
        return visited

    def dijkstra(self, vertex, visited, paths, count):
        counter = 0
        if vertex in visited:
            count += 1
            self.dijkstra(paths[count][0], visited, paths, count)
        else:
            visited.append(vertex)
            if len(paths) == 0:
                sum = 0
                paths.append((vertex, vertex, 0))
            else:
                sum = paths[count][2]
            for i in self.adj_list[vertex]:
                if i[0] not in visited:
                    initial = sum
                    sum += i[1]
                    for j in range(len(paths)):
                        if paths[j][0] == i[0]:
                            if sum < paths[j][2]:
                                paths[j:j + 1] = [(paths[j][0], vertex, sum)]
                            counter += 1
                    if counter == 0:
                        paths.append((i[0], vertex, sum))
                    sum = initial

            count += 1
            if count <= len(paths) - 1:
                self.dijkstra(paths[count][0], visited, paths, count)
            else:
                print("Shortest path(Dijkstra's) Algorithm from vertex C")
                print("Vertex Previous  Distance(From C)")
                for i in range(len(paths)):
                    print(paths[i][0], "       ", paths[i][1], "        ", paths[i][2])


if __name__ == '__main__':
    vertices = ["A", "B", "C", "D", "E", "F"]
    edges = [("A", "B", 13), ("A", "D", 10), ("D", "B", 17), ("E", "B", 20), ("C", "B", 5), ("F", "B", 18),
             ("E", "C", 22), ("F", "C", 30)]
    graph1 = Graph(vertices)
    for x, y, weight in edges:
        graph1.add_edge(x, y, weight)
    graph1.print_adj_List()
    print()
    print("Order in which vertices are visited:", graph1.depth_first_search("C", []))
    print()
    graph1.dijkstra("C", [], [], 0)
