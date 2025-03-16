n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def merge(arr1, arr2):
    temp = []
    idx1 = 0
    idx2 = 0
    
    for _ in range(n+m):
        if idx1 == n:
            temp.append(arr2[idx2])
            idx2 += 1
        elif idx2 == m:
            temp.append(arr1[idx1])
            idx1 += 1
        else:
            if arr1[idx1] <= arr2[idx2]:
                temp.append(arr1[idx1])
                idx1 += 1
            else:
                temp.append(arr2[idx2])
                idx2 += 1
    
    return temp

print(*merge(a, b))