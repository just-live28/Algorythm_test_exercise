n = int(input())
classes = []
for _ in range(n):
    st, en = map(int, input().split())
    classes.append((st, en))
classes.sort(key = lambda x: (x[1], x[0]))

prev_en = 0
result = 0
for st, en in classes:
    if st >= prev_en:
        result += 1
        prev_en = en

print(result)