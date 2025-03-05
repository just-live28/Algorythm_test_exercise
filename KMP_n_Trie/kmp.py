str1 = "ORONDONTISS"
str2 = "NTI"

# 일반적인 패턴 매칭 함수 : O(MN)
# def get_contain_idx(str1, str2):
#     for st in range(len(str1) - len(str2) + 1):
#         match = True
#         for i in range(len(str2)):
#             if str1[st+i] != str2[i]:
#                 match = False
#                 break
#         if match:
#             return True
#     return False

# 실패 함수
def failure_func(string):
    f = [0] * len(string)
    j = 0
    for i in range(1, len(string)):
        while (j > 0 and string[i] != string[j]):
            j = f[j-1]
        if string[i] == string[j]:
            # j는 index이고, f[i]는 글자수이므로 (글자수 = index + 1)
            j += 1
            f[i] = j
    return f

string1 = input()
string2 = input()

def kmp(main, find):
    f = failure_func(find)
    
    j = 0
    for i in range(len(main)):
        while j > 0 and main[i] != find[j]:
            j = f[j-1]
        if main[i] == find[j]:
            j += 1
            if j == len(find):
                return 1
    return 0

print(kmp(string1, string2))