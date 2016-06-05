from queue import Queue
"""
this is a simple bfs implementation in python that takes input of nodes,edges, source and destnations, and prints
the shortest path from source to destination.
"""


def bfs(graph, source, destination):
    distance = [-1] * (len(graph) + 1)  # create a list to save distance from source
    q = Queue()  # queue to save tree level
    distance[source] = 0    # distance of source is 0
    q.put(source)   # put source to queue
    while not q.empty():
        u = q.get()  # get first element of queue and pop it out
        for v in graph[u]:  # explore all the adjacency nodes of u
            if distance[v] == -1:   # if node v is not visited, it is -1
                q.put(v)    # put node v to queue
                distance[v] = distance[u]+1     # distance of v is 1 more than distance of u
                if v == destination:    # destination node reached
                    return distance[v]  # return the destination from source
    return -1   # if destination not found, returns -1


def main():
    node, edge = [int(i) for i in input("enter node and edge:").split()]  # get the number of node & edge
    graph = [[] for i in range(node + 1)]  # create 2D list to store graph
    for i in range(node):
        u, v = [int(i) for i in input("enter connected node1 & node2: ").split()]  # input connected nodes
        graph[u].append(v)
        graph[v].append(u)
    source, destination = [int(i) for i in input("enter stard & end node: ").split()]  # input source & destination
    distance = bfs(graph, source, destination)
    if distance < -1:
        print("source not reachable")
    else:
        print("distance of {} to {} is {}".format(source, destination, distance))


if __name__ == '__main__':
    main()
