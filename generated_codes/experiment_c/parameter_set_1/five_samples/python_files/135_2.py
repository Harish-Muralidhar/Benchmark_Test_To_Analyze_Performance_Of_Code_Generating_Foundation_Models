'''
For second query, 2 is connected to 3 via node 1. Hence distance 2.
For third query, 4 is connected to 3 via node 2. Hence distance 3.

'''

# use a queue
import collections
def find_shortest_path_between_nodes(node_1, node_2):
    # do a BFS starting from node 1 and then check if node is found in the queue when it is being popped
    # if found then return the distance
    q = collections.deque()
    visited = set()
    q.append((node_1, 0))
    visited.add(node_1)
    while q:
        node, dist = q.popleft()
        if node_2 == node:
            return dist
        if 2*node not in visited:
            q.append((2*node, dist+1))
            visited.add(2*node)
        if 2*node+1 not in visited:
            q.append((2*node+1, dist+1))
            visited.add(2*node+1)
    return -1

if __name__ == '__main__':
    num_queries = int(input())
    for _ in range(num_queries):
        node_1, node_2 = map(int, input().split())
        print(find_shortest_path_between_nodes(node_1, node_2))