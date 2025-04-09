n, k = map(int, input().split())

def func(i, stat):
    global RANK, exist
    if stat == n:
        if RANK == k:
            exist = True
            print('+'.join([str(x) for x in arr[:i]]))
        RANK += 1
        return
    elif stat > n:
        return
    
    for j in range(1, 4):
        arr[i] = j
        func(i+1, stat + j)

RANK = 1
exist = False
arr = [0] * 100000
func(0, 0)
if not exist:
    print(-1)