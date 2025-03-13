G = {
    0: [(1, 2), (2, 5)],
    1: [(0, 2), (3, 4), (4, 6)],
    2: [(0, 5), (3, 2), (5, 10)],
    3: [(1, 4), (2, 2), (5, 1), (4, 3)],
    4: [(1, 6), (3, 3), (5, 7)],
    5: [(2, 10), (3, 1), (4, 7)]
}

def Prim(G):
    MST = []
    V = len(G)
    dist = [float('inf') for i in range(V)]
    dist[0] = 0
    prev = [None for i in range(V)]
    S = set()

    while len(S) < V:
        min_dist = float('inf')
        v = -1
        for u in range(V):
            if u not in S and dist[u] < min_dist:
                min_dist = dist[u]
                v = u
        S.add(v)
        if prev[v] is not None:
            MST.append([prev[v], v, dist[v]])
        for u, w in G[v]:
            if u not in S and dist[u] > w:
                dist[u] = w
                prev[u] = v

    return MST
MST = Prim(G)
print(MST)
