# 초밥을 두 배로 늘려서, 끝 요소부터도 슬라이딩 윈도우 할 수 있게끔
# k개 만큼 찝어낸다. 근데 이제 슬라이딩 윈도우를 이용해서, 왼쪽 거 제거하고, 새로 오른쪽 거 추가하고. (집합에)
# 집합의 개수 + (만약 set에 쿠폰 번호가 없다면 + 1) 해서 최대 종류를 기록한다.
# N 접시 수 / d 초밥 가짓수 / k 연속 섭취수 / 쿠폰번호 c

N, d, k, c = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.extend(arr)

species = set()
current = [0] * (d+1)
for i in range(k):
    species.add(arr[i])
    current[arr[i]] += 1
max_result = len(species)
if c not in species:
    max_result += 1

# i가 왼쪽 끝.(즉, arr[i-1]을 species에서 제거.)
# 그리고 arr[i+k-1] 을 species에서 추가
for i in range(1, N):
    deleted_food = arr[i-1]
    current[deleted_food] -= 1
    if current[deleted_food] == 0:
        species.remove(arr[i-1])
    
    added_food = arr[i+k-1]
    species.add(added_food)
    current[added_food] += 1
    
    result = len(species)
    if c not in species:
        result += 1
    
    max_result = max(max_result, result)

print(max_result)