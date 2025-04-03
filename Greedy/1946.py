t = int(input())
for _ in range(t):
    n = int(input())
    people = []
    for _ in range(n):
        a, b = map(int, input().split())
        people.append((a, b))
    people.sort()

    count = 1
    prime_a, prime_b = people[0][0], people[0][1]
    for i in range(1, n):
        _, b = people[i]
        
        if b < prime_b:
            count += 1
            prime_b = b

    print(count)