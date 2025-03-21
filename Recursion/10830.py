n, b = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def make_unit_matrix(k):
    matrix = [[0] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            if i == j:
                matrix[i][j] = 1
    return matrix
            
def multiple_matrix(arr1, arr2):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += (arr1[i][k] * arr2[k][j]) % 1000
    return result

def func(k):
    if k == 0:
        return make_unit_matrix(n)
    
    half = [[x % 1000 for x in row] for row in func(k // 2)]
    if k % 2 == 1:
        return [[x % 1000 for x in row] for row in multiple_matrix(multiple_matrix(arr, half), half)]
    else:
        return [[x % 1000 for x in row] for row in multiple_matrix(half, half)]

for row in func(b):
    print(*row)