answerlist = [0, 0]
def counting(x, y, n):
    check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                for k in range(2):
                    for l in range(2):
                        counting(x + k * n // 2, y + l * n // 2, n // 2)
                return
    answerlist[check] += 1

n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))
counting(0, 0, n)
print(answerlist[0])
print(answerlist[1])