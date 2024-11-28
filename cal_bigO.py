import math

n = int(input())

MAX_LIMIT = int(1e9)

if n**3 <= MAX_LIMIT:
    print("O(N^3)까지 허용됩니다.")
elif n**2 <= MAX_LIMIT:
    print("O(N^2)까지 허용됩니다.")
elif n * math.log2(n) <= MAX_LIMIT:
    print("O(NlogN)까지 허용됩니다.")
elif n <= MAX_LIMIT:
    print("O(N)까지 허용됩니다.")
else:
    print("O(logN)까지만 허용됩니다.")