array = [0] * 20000001

n = int(input())

cards = list(map(int, input().split()))
for i in range(n):
    array[cards[i] + 10000000] += 1

m = int(input())
finds = list(map(int, input().split()))

results = []
for i in range(m):
    results.append(array[finds[i] + 10000000])

for result in results:
    print(result, end=' ')