# By Om Nai

# For creating a graph from the given adjacency matrix
class Graph:
    def __init__(self, graph, num_of_vertex):
        self.g = graph
        self.numberOfVertex = num_of_vertex
        # This is used for keep tracking the visited vertices in BFS traversal
        self.visited = self.numberOfVertex * [0]
        # This is used for getting the parent of the give vertex in the BFS traversal
        self.parent = self.numberOfVertex * [-1]
        # Flow value is set to zero initially
        self.maxFlow = 0
        pass

    # BFS traversal for getting augmenting for the give source/start to sink/destination
    def BFS(self, source, sink):
        # Setting the source vertex path to be visited
        self.visited[source] = 1
        # This list will act as queue data structure
        q = [source]
        while q:
            # Pop the vertex so it will be explored
            vertexToExplore = q.pop(0)
            # The vertex which is being explored so adjacent vertices of that vertex
            for adjVertex in range(0, self.numberOfVertex):
                # If there is no edge between two vertex then it is set to -999
                # Also, value can be 0 or less than that as if after certain amount of flow is passed
                # flow capacity on that edge is reduced
                if self.g[vertexToExplore][adjVertex] > 0 and self.visited[adjVertex] == 0:
                    self.visited[adjVertex] = 1
                    q.append(adjVertex)
                    # Parent vertices to the edge which will lead to destination is stored here
                    self.parent[adjVertex] = vertexToExplore
                    # If path till sink then there is no need of BFS anymore
                    # That is the augmenting path which will lead to the sink.
                    if adjVertex == sink:
                        return True
        # If no path available then false will be returned
        return False

    # Ford Fulkerson algorithm to find the max flow in the graph
    def FordFulkerson(self, source, sink):
        # BFS will be called from source to sink and till it will return false
        # that is no augmenting path available loop will be running
        while self.BFS(source, sink):
            # For getting the path from the parent vertices list
            s = sink
            path = []
            while s != source:
                path.append(self.parent[s])
                s = self.parent[s]

            # This path will be in reversed order and need to reach final sink that will not be present
            # so reversing it and appending sink the sink
            path.reverse()
            path.append(sink)

            # Now, the path from source to sink is obtained so,
            # the capacity between each edge is obtained and stored in the list
            path_capacity = []
            tracker = 0
            # Last one will be the sink to listindexoutofrange element so len(path) - 1
            while tracker != len(path) - 1:
                path_capacity.append(self.g[path[tracker]][path[tracker + 1]])
                tracker += 1

            # tracker will be set to zero,
            # the bottleneck capacity of the augmenting path is found in other words,
            # limit of max flow that can be passed on the given augmenting path is found
            tracker = 0
            bottleNeckCapacity = min(path_capacity)
            self.maxFlow = self.maxFlow + bottleNeckCapacity

            # Now, updating the graph by the backward edges and the subtracting the flow from the forward edges
            while tracker != len(path) - 1:
                self.g[path[tracker]][path[tracker + 1]] -= bottleNeckCapacity
                # If no path between the -999 is set so to set backward edge this is the condition
                if self.g[path[tracker + 1]][path[tracker]] == -999:
                    self.g[path[tracker + 1]][path[tracker]] = bottleNeckCapacity
                # If already backward edge is present
                else:
                    self.g[path[tracker + 1]][path[tracker]] += bottleNeckCapacity
                tracker += 1

            # path is clear so used for next iteration
            path.clear()
            # visited array is reset to 0 so that used for next iteration
            self.visited = self.numberOfVertex * [0]

        # Returning the maximum flow
        return self.maxFlow


if __name__ == "__main__":
    numOfVertex = 6

    adjMatrix = [
        [-999, 16, 13, -999, -999, -999],
        [-999, -999, 10, 12, -999, -999],
        [-999, 4, -999, -999, 14, -999],
        [-999, -999, 9, -999, -999, 20],
        [-999, -999, -999, 7, -999, 4],
        [-999, -999, -999, -999, -999, -999]
    ]

    graph1 = Graph(adjMatrix, numOfVertex)
    print("The max flow is : ", graph1.FordFulkerson(0, 5))
