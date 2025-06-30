n = int(input())
words = []
arr = [0] * 91
for _ in range(n):
    word = input()
    words.append(word)
    size = len(word)
    for i in range(size):
        arr[ord(word[i])] += 10 ** (size-1-i)

# arr[65:91]
char_arr = []
for i in range(65, 91):
    char_arr.append((chr(i), arr[i]))
char_arr.sort(key = lambda x : -x[1])

dic = {}
num = 9
for c, _ in char_arr:
    dic[c] = num
    num -= 1

    if num == -1:
        break

result = 0
for word in words:
    size = len(word)
    for i in range(size):
        result += dic[word[i]] * (10 ** (size - 1 - i))
print(result)