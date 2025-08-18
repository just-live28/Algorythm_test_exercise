n = int(input())
arr = list(map(int, input().split()))

result = 0
chk = [False] * 100002
st = en = 0

while en < n:
    num = arr[en]
    
    while chk[num]:
        chk[arr[st]] = False
        st += 1
    
    chk[num] = True
    result += en - st + 1
    en += 1
        
print(result)