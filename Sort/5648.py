import sys
input = sys.stdin.readline
INF = int(1e9)

n = INF
count = 0
result = []
while count < n:
    line = input().rstrip().split()
    
    if n == INF:
        n = int(line[0])
        
        line = line[1:]
    
    for num in line:
        num = int(''.join(reversed([x for x in num])))
        result.append(num)
        count += 1

result.sort()
for i in result:
    print(i)