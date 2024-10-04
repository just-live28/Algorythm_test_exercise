# d[n] = d[n-2] * 2 + d[n-1] 

# d[0] = 0, d[1] = 1, d[2] = 3, d[3] = 5

n = int(input())

d = [0] * (n+1)

d[1], d[2] = 1, 3

for i in range(3, n+1):
    d[i] = (d[i-2] * 2 + d[i-1]) % 796796


print(d[n])