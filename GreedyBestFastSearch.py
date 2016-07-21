distance = {
    'a': 366,
    'b': 0,
    'c': 160,
    'd': 242,
    'e': 161,
    'f': 176,
    'g': 77,
    'h': 151,
    'i': 226,
    'l': 244,
    'm': 241,
    'n': 234,
    'o': 380,
    'p': 10,
    'r': 193,
    's': 253,
    't': 329,
    'u': 80,
    'v': 199,
    'z': 374
}

adj = {
    'a': ['s', 't', 'z'],
    'b': ['u', 'g', 'p', 'f'],
    'c': ['d', 'r', 'p'],
    'd': ['c', 'm'],
    'e': ['h'],
    'f': ['b', 's'],
    'g': ['b'],
    'h': ['e', 'u'],
    'i': ['n', 'v'],
    'l': ['m', 't'],
    'm': ['d', 'l'],
    'n': ['i'],
    'o': ['s', 'z'],
    'p': ['b', 'c', 'r'],
    'r': ['c', 'p,', 's'],
    's': ['a', 'f', 'o', 'r'],
    't': ['a', 'l'],
    'u': ['b', 'h', 'v'],
    'v': ['i', 'u'],
    'z': ['a', 'o']
}

source_to_destination_distance = 0
path = list()


def greedy_best_fast_search(source_city, destination_city):
    global source_to_destination_distance
    # if the city is reached, no need to search further
    if source_city == destination_city:
        return
    # temporarily store adjacent cities to a dictionary
    adj_city = dict()
    for city in adj[source_city]:
        adj_city[city] = distance[city]

    '''debug
    print(adj_city)'''
    # get the nearest city according to distance
    nearest_city = sorted(adj_city, key=adj_city.__getitem__)
    source_to_destination_distance = source_to_destination_distance + distance[nearest_city[0]]
    '''debug
    print(adj_city)'''
    # append the nearest city to path
    path.append(nearest_city[0])
    # call greedy_best_fast_search() for the nearest city again
    greedy_best_fast_search(nearest_city[0], destination_city)


def main():
    global path
    source = 'a'
    destination = 'b'
    path.append(source)
    greedy_best_fast_search(source, destination)
    total_city_in_path = len(path)
    for c in range(total_city_in_path-1):
        print(path[c], end='->')
    print(path[total_city_in_path-1])
    # print(source_to_destination_distance)

if __name__ == '__main__':
    main()




