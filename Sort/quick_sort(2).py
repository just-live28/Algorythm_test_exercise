array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_array = [x for x in tail if x <= pivot]
    right_array = [x for x in tail if x > pivot]
    
    return quick_sort(left_array) + [pivot] + quick_sort(right_array)

print(quick_sort(array))
    