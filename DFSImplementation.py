"""
this simple program describes the basic concept of DFS. it takes input of nodes & edges and prints the traversal routes.
"""

graph = []  # list to store 2D graph
parent = []     # list to store parent
visit = []      # list to check if visited or not


def dfs(u):
    global parent   # global access to edit
    global visit    # global access to edit
    if visit[u]:    # node already visited, returns from here
        return
    visit[u] = True     # node is visited
    print(u, "->", end="")
    for v in graph[u]:
        parent[v] = u       # set u as parent of v
        dfs(v)      # recursively calls dfs


def main():
    global graph    # global access to edit
    global parent   # global access to edit
    global visit    # global access to edit
    node, edge = [int(i) for i in input("enter node & edge: ").split()]     # input nodes & edges
    graph = [[] for i in range(node+1)]
    for i in range(edge):
        u, v = [int(i) for i in input("enter node1--->node2: ").split()]    # enter u-->v nodes
        graph[u].append(v)
    visit = [False]*(node+1)    # initially no nodes are visited
    parent = [-1]*(node+1)      # initially no parent (-1)
    for u in range(node):
        if not visit[u]:
            dfs(u)      # calling dfs


if __name__ == '__main__':
    main()
