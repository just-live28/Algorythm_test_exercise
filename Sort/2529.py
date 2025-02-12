k = int(input())
opers = list(input().split())

max_num = 0
min_num = int(1e10)

def func(n, string):
    global max_num, min_num
    if n == k+1:
        result = int(string)
        max_num = max(result, max_num)
        min_num = min(result, min_num)
        return
    
    for i in range(10):
        if visited[i] == False:
            if opers[n-1] == '>' and int(string[n-1]) > i:
                visited[i] = True
                func(n+1, string + str(i))
                visited[i] = False
            elif opers[n-1] == '<' and int(string[n-1]) < i:
                visited[i] = True
                func(n+1, string + str(i))
                visited[i] = False

for j in range(10):
    visited = [False] * 10
    visited[j] = True
    func(1, str(j))

print(str(max_num).zfill(k+1))
print(str(min_num).zfill(k+1))