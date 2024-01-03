infinity = float("inf")

# PROBLEM # 1
# graph = {
#     'start': {
#         'a': 6,
#         'b': 2
#     },
#     'a': {
#         'fin': 1
#     },
#     'b': {
#         'a': 3,
#         'fin': 5
#     },
#     'fin': {}
# }

# costs = {
#     'a': 6,
#     'b': 2,
#     'fin': infinity
# }

# parents = {
#     'a': 'start',
#     'b': 'start',
#     'fin': None
# }

# PROBLEM # 2
# graph = {
#     'start': {
#         'a': 5,
#         'c': 2
#     },
#     'a': {
#         'b': 4,
#         'd': 2,
#     },
#     'b': {
#         'd': 6,
#         'fin': 3
#     },
#     'c': {
#         'a':8,
#         'd':7
#     },
#     'd': {
#         'fin': 1
#     },
#     'fin': {}
# }

# costs = {
#     'a': 5,
#     'c': 2,
#     'b': infinity,
#     'd': infinity,
#     'fin': infinity
# }

# parents = {
#     'a': 'start',
#     'c': 'start',
#     'b': None,
#     'd': None,
#     'fin': None
# }

# PROBLEM # 3
# graph = {
#     'start': {
#         'a': 10
#     },
#     'a': {
#         'b': 20
#     },
#     'b': {
#         'c': 1,
#         'fin': 30
#     },
#     'c': {
#         'a':1
#     },
#     'fin': {}
# }

# costs = {
#     'a': 10,
#     'b': infinity,
#     'c': infinity,
#     'fin': infinity
# }

# parents = {
#     'a': 'start',
#     'b': None,
#     'c': None,
#     'fin': None
# }

# PROBLEM # 4
graph = {
    'start': {
        'a': 2,
        'b': 2
    },
    'a': {
        'c': 2,
        'fin': 2
    },
    'b': {
        'a': 2
    },
    'c': {
        'b':-1,
        'fin':2
    },
    'fin': {}
}

costs = {
    'a': 2,
    'b': 2,
    'c': infinity,
    'fin': infinity
}

parents = {
    'a': 'start',
    'b': 'start',
    'c': None,
    'fin': None
}

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def dijkstra_search(finish):
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if (costs[n] > new_cost):
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    return costs[finish]

print('time to fin:', dijkstra_search('fin'))
node = 'fin'
route = [node]
while node != 'start':
    node = parents[node]
    route.append(node)
route.reverse()
print(' - '.join(route))