n = int(input())
quad_tree = []
for _ in range(n):
    quad_tree.append(list(input()))
answer = ''

def func(row, col, num):
    check = quad_tree[row][col]
    for i in range(row, row + num):
        for j in range(col, col + num):
            if check != quad_tree[i][j]:
                newnum = num // 2
                answer = ('('
                          + func(row, col, newnum)
                          + func(row, col + newnum, newnum)
                          + func(row + newnum, col,newnum)
                          + func(row + newnum, col + newnum, newnum)
                          + ')')
                return answer
    else:
        answer = check
        return answer

print(func(0, 0, n))