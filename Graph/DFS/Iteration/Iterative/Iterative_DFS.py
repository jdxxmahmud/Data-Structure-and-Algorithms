# iterative BFS
def DFS(adjList, startNode, visited):

    visSequence = []

    visited[startNode] = True
    
    stack = [startNode]

    while stack:

        node = stack.pop()

        print(f"Visiting: {node}")

        visSequence.append(node)

        for neighbor in adjList[node]:

            if not visited[neighbor]:

                stack.append(neighbor)

                visited[neighbor] = True


    return visSequence


'''
# Function to add an edge to the directed graph
def addEdge(adjList, u, v):
    adjList[u].append(v)
'''


# Function to add an edge to the undirected graph
def addEdge(adjList, u, v):
    adjList[u].append(v)
    adjList[v].append(u)

def main():
    # Number of vertices in the graph
    vertices = 5

    # Adjacency list representation of the graph
    adjList = [[] for _ in range(vertices)]

    # Add edges to the graph
    addEdge(adjList, 0, 1)
    addEdge(adjList, 0, 2)
    addEdge(adjList, 1, 2)
    addEdge(adjList, 1, 3)
    addEdge(adjList, 2, 4)
    addEdge(adjList, 3, 4)


    # Mark all the vertices as not visited
    visited = [False] * vertices

    startNode = 4

    # Perform BFS traversal starting from vertex 0
    print(f"Depth First Traversal starting from vertex {startNode}")

    visitingSequence = DFS(adjList, startNode, visited)

    visSeqStr = " -> ".join(map(str, visitingSequence))

    print(f"The visiting sequence is: {visSeqStr}")


if __name__ == "__main__":
    main()