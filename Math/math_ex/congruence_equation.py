def check():
    i = 9
    while i < 30:
        if i % 5 == 2:
            return i
        i += 6
    return -1

print(check())