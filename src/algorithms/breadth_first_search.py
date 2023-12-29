from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['tom','johnny']
graph['anuj'] = []
graph['peggy'] = []
graph['tom'] = []
graph['johnny'] = []

def person_is_seller(person):
    return person == 'aaa'

def breadth_first_search(graph):
    search_queue = deque()
    search_queue += graph['you']
    searched = []
    
    while search_queue:
        person = search_queue.popleft()
        if person in searched:
            continue
        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        else:
            search_queue += graph[person]
            searched.append(person)
    return False

print(breadth_first_search(graph), 'peggy')