# iterative BFS
from collections import deque

def BFS(adjList, startNode, visited):

    # This shows the sequence of nodes being visited. This will be returned by the function
    visSequence = []
    
    qu = deque()

    visited[startNode] = True
    qu.append(startNode)

    while qu:

        # getting the first element in the queue
        visNode = qu.popleft()

        # Inserting in the visited sequence
        visSequence.append(visNode)

        # Inserting the "Unvisited" neighbors in the queue
        for neighbor in adjList[visNode]:
            
            if not visited[neighbor]:
                qu.append(neighbor)

                # Marking the neighbor node as visited
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

    # Perform BFS traversal starting from vertex 0
    print("Breadth First Traversal starting from vertex 0")


    visitingSequence = BFS(adjList, 4, visited)

    visSeqStr = " -> ".join(map(str, visitingSequence))

    print(f"The visiting sequence is: {visSeqStr}")


if __name__ == "__main__":
    main()