
# A, B를 작은 순 정렬
# B 포인터 값이 A 포인터 값보다 같거나 클 때까지 B 포인터를 옮기기
# 현재 B 포인터만큼 쌍 수 계산
# B 포인터가 끝에 다다른 경우, 남은 A 포인터에 대해서는 B포인터 값만큼 계산

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()

    count = 0
    b_idx = 0
    for i in range(n):
        while b_idx < m and a[i] > b[b_idx]:
            b_idx += 1
        
        count += b_idx

    print(count)