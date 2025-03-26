def multiple_matrix(arr1, arr2):
    row = len(arr1)
    col = len(arr2[0])
    items = len(arr1[0])
    
    matrix = [[0] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            result = 0
            for k in range(items):
                result += arr1[i][k] * arr2[k][j]
            matrix[i][j] = result % 1000
    return matrix
                
def make_unit_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 1
    return matrix

def func(arr, b):
    if b == 0:
        return make_unit_matrix(n)
    
    half = func(arr, b // 2)
    if b % 2 == 1:
        return multiple_matrix(arr, multiple_matrix(half, half))
    else:
        return multiple_matrix(half, half)
    
n, b = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

result = func(arr, b)
for line in result:
    print(*line)