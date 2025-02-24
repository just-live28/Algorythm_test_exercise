import sys
input = sys.stdin.readline

n = int(input())
entered = {}
for _ in range(n):
    name, stat = input().split()
    if stat == "leave" and name in entered:
        del entered[name]
    elif stat == "enter" and name not in entered:
        entered[name] = 1

arr = list(entered.keys())
arr.sort(reverse = True)
for name in arr:
    print(name)