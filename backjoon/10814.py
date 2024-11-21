n = int(input())

persons = []
for i in range(n):
    a, b = input().split()
    persons.append((int(a), b, i))

persons.sort(key = lambda x : (x[0], x[2]))

for person in persons:
    print(person[0], person[1])