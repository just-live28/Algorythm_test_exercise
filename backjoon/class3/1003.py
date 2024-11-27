dp_0 = [-1] * 41
dp_1 = [-1] * 41

dp_0[0], dp_1[0] = 1, 0
dp_0[1], dp_1[1] = 0, 1

def fibonacci(n):
    dp_0[n] = dp_0[n-1] + dp_0[n-2]
    dp_1[n] = dp_1[n-1] + dp_1[n-2]

for i in range(2, 41):
    fibonacci(i)

tc = int(input())
for _ in range(tc):
    num = int(input())
    print(dp_0[num], dp_1[num])