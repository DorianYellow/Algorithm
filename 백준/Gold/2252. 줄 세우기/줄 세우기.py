from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

anslist = []
while q:
    curr = q.popleft()
    anslist.append(curr)
    for x in graph[curr]:
        indegree[x] -= 1
        if indegree[x] == 0:
            q.append(x)

print(*anslist)