import copy

def swap(array, n):
    global result
    
    if n == max_swap:
        total = 0
        
        product_size = 0
        for i in range(len(array)-1, -1, -1):
            total += array[i] * (10**product_size)
            product_size += 1
        
        if len(array) == 2:
            result = total
        elif total > result:
            result = total
        
        return
    
    enable = False
    array = copy.deepcopy(array)
    for i in range(0, len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] < array[j]:
                enable = True
                array[i], array[j] = array[j], array[i]
                swap(array, n+1)
    
    if enable == False:
        array[-1], array[-2] = array[-2], array[-1]
        swap(array, n+1)

T = int(input())

results = []
for _ in range(T):
    numbers, n = input().split()
    max_swap = int(n)
    result = 0

    arr = []
    for i in range(len(numbers)):
        arr.append(int(numbers[i]))
        
    swap(arr, 0)
    results.append(result)

for i in range(len(results)):
    print("#" + str(i+1) + " " + str(results[i]))