n = int(input())
arr = list(map(int, input().split()))
target = int(input())

table = {}
for i in arr:
    table[target - i] = 1

count = 0
for i in arr:
    if i == target - i:
        continue
    if i in table:
        count += 1
        del table[target-i]
        
print(count)