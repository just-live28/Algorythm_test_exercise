t = int(input())
n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

n_sums = [0] * (n+1)
for i in range(1, n+1):
    n_sums[i] = n_sums[i-1] + n_arr[i-1]
m_sums = [0] * (m+1)
for i in range(1, m+1):
    m_sums[i] = m_sums[i-1] + m_arr[i-1]

dic = {}
for j in range(1, n+1):
    for i in range(1, j+1):
            result = n_sums[j] - n_sums[i-1]
            dic[result] = dic.get(result, 0) + 1

total_count = 0
for j in range(1, m+1):
    for i in range(1, j+1):
        result = m_sums[j] - m_sums[i-1]
        
        if t - result in dic:
            total_count += dic[t - result]

print(total_count)