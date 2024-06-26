from collections import deque
import sys
input = sys.stdin.readline

l, w = map(int, input().split())
treasure_map = []
for _ in range(l):
    treasure_map.append(list(input()))

dx = [-1,0,1,0]#[1,-1,0,0]
dy = [0,1,0,-1]#[0,0,1,-1]

tmp = 0
tmp_visited = [[False] * w for _ in range(l)]
candidates = []
for i in range(l):
    for j in range(w):
        if treasure_map[i][j] == 'L' and not tmp_visited[i][j]:
            tmp_visited[i][j] = True
            q = deque([(i,j,0)])
            while q:
                now_x, now_y, distance = q.popleft()
                if distance > tmp:
                    tmp = distance
                    candidates.append((now_x, now_y))
                for k in range(4):
                    next_x = now_x + dx[k]
                    next_y = now_y + dy[k]
                    if 0 <= next_x < l and 0 <= next_y < w and treasure_map[next_x][next_y] =='L' and not tmp_visited[next_x][next_y]:
                        tmp_visited[next_x][next_y] = True
                        q.append((next_x, next_y, distance + 1))

ans = 0
for i,j in candidates:
    tmp_visited = [[False] * w for _ in range(l)]
    tmp_visited[i][j] = True
    q = deque([(i, j, 0)])
    while q:
        now_x, now_y, distance = q.popleft()
        if distance > ans:
            ans = distance
        for k in range(4):
            next_x = now_x + dx[k]
            next_y = now_y + dy[k]
            if 0 <= next_x < l and 0 <= next_y < w and treasure_map[next_x][next_y] == 'L' and not tmp_visited[next_x][next_y]:
                tmp_visited[next_x][next_y] = True
                q.append((next_x, next_y, distance + 1))
print(ans)