import sys
input = lambda:sys.stdin.readline().rstrip()

N = int(input())
coordinates = []
for _ in range(N):
    x, y = map(int,input().split())
    coordinates.append((x,y))
coordinates.sort()
for coordinate in coordinates:
    print(*coordinate)