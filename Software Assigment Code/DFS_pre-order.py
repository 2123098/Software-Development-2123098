#Using the DFS to travel deep and Pre-order Traversal method to visit every city

#Pseudocode
#Leeds is connected to Monrovia and London
#Monrovia is connected to Madrid and Warsaw
#Madrid is connected to Rome and Tirana 
#Rome connects to none 
#Tirana connects to none 
# Warsaw connects to none  
#London is connected to Paris and New York 
#Paris is connected to Islamabad and Berlin 
#Islamabad connects to none 
#Berlin connects to none  
#New York is connected to Washington DC and Tokyo 
#Washington DC connects to none 
#Tokyo connects to none  

# Using a Python dictionary to act as an adjacency list
graph = {
    "9": ["5","14"],
    "5": ["3", "6"],
    "3": ["1", "4"],
    "1": [],
    "4": [],
    "6": [],
    "14": ["11", "17"],
    "11": ["10", "12"],
    "10": [],
    "12": [],
    "17": ["15", "19"],
    "15": [],
    "19": []
}
print(graph)


# Set to keep track of visited nodes of graph.
visitednode = set()

#function for dfs
def dfs(visitednode, graph, rootnode):
    if rootnode not in visitednode:
        print(rootnode)
        visitednode.add(rootnode)
        for childnode in graph[rootnode]:
            dfs(visitednode, graph, childnode)
print("DFS Pre order result is:")


# Driver Code
dfs(visitednode, graph, "9")




