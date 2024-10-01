# 부품 N개, M종류의 부품을 대량 구매
# 각각 검색 후 있으면 yes, 없으면 no를 출력(한 줄로)

n = int(input())
stores = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while(start <= end):
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

results = []
for target in targets:
    result = binary_search(stores, target, 0, n-1)
    
    if result == None:
        results.append("no")
    else:
        results.append("yes")

for result in results:
    print(result, end=' ')