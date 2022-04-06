# Graph implementation
nodes = ('A', 'B', 'C', 'D', 'E', 'Z')
distances = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'Z': 6},
    'E': {'C': 10, 'D': 2, 'Z': 5},
    'Z': {'D': 6, 'E': 5}}

# using None as +inf
unvisited = {node: None for node in nodes}
visited = {}
current = 'A'
currentDistance = 0
unvisited[current] = currentDistance

# Dijkstra's algorithm
while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

# Print the Shortest Path
print(visited)