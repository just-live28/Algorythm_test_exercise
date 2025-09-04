# 상담은 현재 일자를 포함
# 미래의 선택에 따라 분기가 폭발적으로 증가 → 역으로 계산하기
# 미래에서 벌 수 있는 최대 금액: future_earn
# d[i] : i 일에서부터 벌 수 있는 최대 금액
# ti, pi
# i + ti - 1 라면, d[i] = max(future_earn, d[i + ti] + pi)
# 아니라면 d[i] = future_earn
# 이후 future_earn도 갱신

n = int(input())
times = [None]
pays = [None]
for _ in range(n):
    t, p = map(int, input().split())
    times.append(t)
    pays.append(p)

d = [0] * 20
future_earn = 0
for i in range(n, 0, -1):
    if i + times[i] -1 <= n:
        d[i] = max(future_earn, d[i + times[i]] + pays[i])
    else:
        d[i] = future_earn
    
    future_earn = d[i]

print(d[1])