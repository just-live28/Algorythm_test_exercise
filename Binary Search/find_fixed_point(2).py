# 중간 인덱스를 확인. 그 값이 더 작다면? 오른쪽으로
# 그 값이 더 크다면, 왼쪽으로

n = int(input())
array = list(map(int, input().split()))

def find_fixed_point(array, start, end):
    while(start <= end):
        mid = (start + end) // 2
        
        if array[mid] == mid:
            return mid
        elif array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return None

result = find_fixed_point(array, 0, n-1)

if result == None:
    print(-1)
else:
    print(result)