"""

"""

import sys
import math
import heapq

def dijkstra(graph, start, end):
    # initialize
    dist = {}
    prev = {}
    Q = []
    for v in graph:
        dist[v] = math.inf
        prev[v] = None
        heapq.heappush(Q, (dist[v], v))
    dist[start] = 0

    # main loop
    while Q:
        u = heapq.heappop(Q)[1]
        if u == end:
            break
        for v in graph[u]:
            alt = dist[u] + graph[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(Q, (dist[v], v))
    return dist, prev

def main():
    N = int(input())
    values = [int(x) for x in input().split()]
    graph = {}
    for i in range(N):
        graph[i+1] = {}
    for i in range(N-1):
        u, v = [int(x) for x in input().split()]
        graph[u][v] = values[u-1] * values[v-1]
        graph[v][u] = values[u-1] * values[v-1]
    Q = int(input())
    for i in range(Q):
        M, x, y = [int(x) for x in input().split()]
        values = [int(x) for x in input().split()]
        for j in range(M):
            v = values[j]
            dist, prev = dijkstra(graph, 1, v)
            print(dist)
            print(prev)

if __name__ == "__main__":
    main()