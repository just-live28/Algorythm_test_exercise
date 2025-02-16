n = int(input())

def hanoi(n, a, b):
    if n == 1:
        print(a, b)
        return
    
    hanoi(n-1, a, 6-(a+b))
    print(a, b)
    hanoi(n-1, 6-(a+b), b)

print((1 << n) - 1)
hanoi(n, 1, 3)