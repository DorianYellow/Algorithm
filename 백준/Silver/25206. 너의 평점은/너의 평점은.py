grade_dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

ans = 0
total_num = 0
for _ in range(20):
    _, num, grade = input().split()
    if grade == 'P':
        continue
    total_num += float(num)
    ans += float(num) * grade_dic[grade]
print(ans / total_num)
