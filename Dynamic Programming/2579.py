# 규칙
# 한 번에 한개, 또는 두개씩 오를 수 있음.
# 연속된 3개의 계단을 모두 밟으면 안됨. -> 111 안됨
# 밟는다 : 현재값 + (2,1), 현재값 + (1,2)
# 안밟는다 : (1, 1)

# 테이블
# d[k] : k번째 계단에서 얻을 수 있는 최대 점수

# 점화식
# d[k] = max(arr[k] + d[k-2] + d[k-3], arr[k] + d[k-1] + d[k-3], d[k-1] + d[k-2])

# 초기값 

# , (d-3, -1, 0), (d-2, 0),

n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

d = [0] * 301
d[1] = arr[1]
if n >= 2:
    d[2] = arr[1] + arr[2]
if n >= 3:
    for i in range(3, n+1):
        d[i] = max(d[i-3] + arr[i-1] + arr[i], d[i-2] + arr[i])
    
print(d[n])