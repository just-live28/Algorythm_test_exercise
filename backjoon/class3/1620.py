n, m = map(int, input().split())

array = [None]
dictionary = {}

for i in range(1, n+1):
    name = input()
    array.append(name)
    dictionary[name] = i

for _ in range(m):
    question = input()
    
    if question.isnumeric():
        print(array[int(question)])
    else:
        print(dictionary[question])