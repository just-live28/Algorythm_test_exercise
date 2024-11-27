import sys
input = sys.stdin.readline

a = set()
b = set()

n, m = map(int, input().split())

for _ in range(n):
    a.add(input().replace('\n', ''))

for _ in range(m):
    b.add(input().replace('\n', ''))
    
c = list(a & b)
c.sort()

print(len(c))
for i in c:
    print(i)