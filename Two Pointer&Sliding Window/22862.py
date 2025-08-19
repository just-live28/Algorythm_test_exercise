n, k = map(int, input().split())
arr = list(map(int, input().split()))

## 1번 풀이 ##
# odd = 0
# st = en = 0
# result = 0
# even_length = 0
# while en < n:
#     if arr[en] % 2 == 0:
#         even_length += 1
#         result = max(result, even_length)
#     else:
#         odd += 1
        
#         while odd > k:
#             if arr[st] % 2 == 1:
#                 odd -= 1
#             else:
#                 even_length -= 1
#             st += 1
    
#     en += 1

# print(result)

## 2번 풀이 ##
# odd = arr[0] % 2
# result = 0
# en = 0
# for st in range(n):
#     while en < n-1 and arr[en+1] % 2 + odd <= k:
#         en += 1
#         odd += arr[en] % 2
#     result = max(result, en - st + 1 - odd)
#     odd -= arr[st] % 2

# print(result)

## 3번 풀이 ##
odd = 0
st = 0
result = 0
for en in range(n):
    odd += arr[en] % 2
    result = max(result, en - st + 1 - odd)
        
    while odd > k:
        odd -= arr[st] % 2
        st += 1

print(result)