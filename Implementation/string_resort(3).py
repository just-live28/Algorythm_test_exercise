string = input()

alphas = []
numbers = []
for i in range(len(string)):
    if string[i].isalpha():
        alphas.append(string[i])
    else:
        numbers.append(int(string[i]))

alphas.sort()
alphas.append(str(sum(numbers)))

for i in range(len(alphas)):
    print(alphas[i], end='')