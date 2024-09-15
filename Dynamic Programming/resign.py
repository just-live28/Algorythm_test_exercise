import sys
input = sys.stdin.readline

array = []
array.append((0,0))

n = int(input())
d = [0] * (n+1)
for i in range(1,n+1):
    t, p = map(int,input().split())
    # 인덱스 i에 (걸리는 시간(Ti), 버는 돈(Pi))
    array.append((t,p))

def counsel(prev_earn, start):
    end = start + array[start][0] - 1
    if end <= n:
        earn = prev_earn + array[start][1]
        if earn > d[end]:
            d[end] = earn
        for i in range(end+1, n+1):
            counsel(earn, i)
    else:
        if prev_earn > d[start]:
            d[start] = prev_earn

for i in range(1, n+1):
    counsel(0, i)
        
print(max(d))