# 하나는 작은 순으로, 다른 하나는 큰 순으로 정렬
# 이후 요소끼리 곱해서 합해주면 된다.

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.sort()
arr2.sort(reverse=True)

result = 0
for i in range(n):
    result += arr1[i] * arr2[i]

print(result)