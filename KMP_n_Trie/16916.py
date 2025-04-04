word1 = input()
word2 = input()

def failure(s):
    f = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = f[j-1]
        if s[i] == s[j]:
            j += 1
            f[i] = j
    return f

def kmp(s1, s2):
    f = failure(s2)
    j = 0
    table = [0] * len(s1)
    for i in range(len(s1)):
        while j > 0 and s1[i] != s2[j]:
            j = f[j-1]
        if s1[i] == s2[j]:
            j += 1
            table[i] = j
            if j == len(s2):
                return table
    return table

print(failure(word2))
print(kmp(word1, word2))