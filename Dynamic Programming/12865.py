# 최대 무게 k

# 물건의 무게 w

# w부터 k-w까지 비교가 가능
# -> 무게는 k~w까지 (역순순)
# d[i] = max(d[i], d[i-w] + value)

# 큰 쪽부터. k부터 시작해서 w까지 내려와야 한다.
# 먼젓번 게 갱신되면, 갱신된 것을 토대로 다음번 것들이 갱신되기 때문에 중복 값이 더해질 수 있다.
# d[k] = max(d[k], d[k-w] + value)
# d[w] = max(d[w], d[])

n, k = map(int, input().split())
d = [0] * 100001
for _ in range(n):
    w, v = map(int, input().split())
    for i in range(k, w-1, -1):
        d[i] = max(d[i], d[i-w] + v)

print(d[k])