n = int(input())
line = list(input().split())
dic = {}
for i in line:
    dic[i] = 0

for _ in range(n):
    line = list(input().split())

    for i in line:
        dic[i] += 1

result = []
for name, like in dic.items():
    result.append((name, like))

result.sort(key = lambda x : (-x[1], x[0]))
for name, like in result:
    print(name, like)