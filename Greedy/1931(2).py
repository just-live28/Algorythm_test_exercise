n = int(input())
conventions = []
for _ in range(n):
    st, en = map(int, input().split())
    conventions.append((st, en))
conventions.sort(key = lambda x : (x[1], x[0]))

cur = -1
count = 0
for start, end in conventions:
    if start >= cur:
        count += 1
        cur = end

print(count)