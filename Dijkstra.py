#G = [
#    [(1, 2), (2, 4)],
#  [(2, 1), (3, 7)],
#   [(3, 3)],
#   [(4, 2)],
#   []
#]
G = [
    [(1,1.5), (4,0.5)],
    [(2,1), (3,3)],
    [(3,1)],
    [(0,2)],
    [(1, 0.5)],
    [(4,1)]
]

def Dijkstra(G, s):
    V = len(G)
    dist = [float('inf') for i in range(V)]
    dist[s] = 0
    S = set()
    while len(S) < V:
        min_dist = float('inf')
        v = -1
        for i in range(V):
            if i not in S and dist[i] < min_dist:
                min_dist = dist[i]
                v = i
        S.add(v)
        for u, w in G[v]:
            if u not in S and dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
    return dist

print(Dijkstra(G, 0))
