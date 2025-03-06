k = int(input())

golds = []
for _ in range(k):
    n = int(input())
    if n == 0:
        golds.pop()
    else:
        golds.append(n)
print(sum(golds))