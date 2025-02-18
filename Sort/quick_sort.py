array = [6, -8, 1, 12, 8, 3, 7, -7]

def quick_sort(start, end):
    if start >= end - 1:
        return
    
    lidx = start + 1
    ridx = end - 1
    pivot = array[start]
    while True:
        while (lidx <= ridx and array[lidx] <= pivot):
            lidx += 1
        while (lidx <= ridx and array[ridx] > pivot):
            ridx -= 1
        if lidx > ridx:
            break
        array[lidx], array[ridx] = array[ridx], array[lidx]
    array[start], array[ridx] = array[ridx], array[start]
    
    quick_sort(start, ridx)
    quick_sort(ridx+1, end)

quick_sort(0, len(array))
print(array)