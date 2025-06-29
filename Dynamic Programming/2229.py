n = int(input())
arr = list(map(int, input().split()))

def cal_diff(st, en):
    max_num = -1
    min_num = 10001

    for num in arr[st:en+1]:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
    
    return max_num - min_num

d = [0] * (n+1)

for i in range(1, n+1):
    d[i] = cal_diff(0, i)
    for j in range(1, i+1):
        d[i] = max(d[i], d[j-1] + cal_diff(j, i))

print(d[n])