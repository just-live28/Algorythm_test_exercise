def cal_count(n):
    if n == 1:
        return 1
    
    return 2 * cal_count(n-1) + 1

def hanoi(n, a, b):
    if n == 1:
        print(a, b)
        return
    
    mid = 6 - (a + b)
    
    hanoi(n-1, a, mid)
    print(a, b)
    hanoi(n-1, mid, b)

n = int(input())
print(cal_count(n))
hanoi(n, 1, 3)