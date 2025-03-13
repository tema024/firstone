#       7
#      6  9
#     2    3
#    1 4
#     5
graph = {7:[6,9],
         6:[2],
         9:[3],
         2:[1,4],
         1:[5],
         4:[],
         5:[],
         3:[]}

def BFS(graph, start):
    visited = set()
    queue = []
    queue.append(start)
    visited.add(start)
    result = []

    while queue:
        node = queue.pop(0)
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

print(BFS(graph,7))
