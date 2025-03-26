# 배열의 총 개수 구하기

word = "moo"
arr = [3]
cur = 3
i = 0
while arr[-1] <= int(1e9):
    i += 1
    arr.append(2 * arr[i-1] + 1 + (i + 2))

n = int(input())
arr_num = 0
while arr[arr_num] <= n:
    arr_num += 1

def moo(k, idx):
    if k == 0:
        return word[idx]
    
    if 0 <= idx <= arr[k-1] - 1:
        return moo(k-1, idx)
    elif arr[k-1] <= idx <= arr[k-1] + (k + 2):
        if idx == arr[k-1]:
            return 'm'
        else:
            return 'o'
    else:
        return moo(k-1, idx - (arr[k-1] + (k+3)))

print(moo(arr_num, n-1))