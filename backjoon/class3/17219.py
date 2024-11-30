n, m = map(int, input().split())

array = {}

for _ in range(n):
    a, b = input().split()    
    array[a] = b

for _ in range(m):
    print(array[input()])