class Graph:

    def __init__(self):
        
        self.graph = dict()

    def add_edge(self, u, v):

        try:
            self.graph[u].append(v)
        except:
            self.graph[u] = [v]

    def BFS(self, source):

        visited = [False]* len(self.graph)

        queue = list()
        queue.append(source)

        while queue:

            vertex = queue.pop(0)
            visited[vertex] = True
            print(str(vertex)+" visited")

            for i in self.graph[vertex]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)


if __name__ == "__main__":
    
    g = Graph() 
    g.add_edge(0, 1) 
    g.add_edge(0, 2) 
    g.add_edge(1, 2) 
    g.add_edge(2, 0) 
    g.add_edge(2, 3) 
    g.add_edge(3, 3) 

    g.BFS(2)

    