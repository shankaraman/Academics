import random
def Merge(left, right, array):
    left_size, right_size = len(left), len(right)
    i = j = k = 0
    while (i< left_size and j < right_size):
        if (left[i] <= right[j]):
            array[k] = left[i]
            k+=1;i+=1
        else:
            array[k] = right[j]
            k+=1;j+=1

    while i < left_size:
        array[k] = left[i]
        i+=1;k+=1

    while j < right_size:
        array[k] = right[j]
        j+=1;k+=1

def MergeSort(array):
    n = len(array)
    if n < 2:
        return
    left_array, right_array, mid, i = [], [], n/2, 0
    while i < mid:
        left_array.append(array[i])
        i+=1
    i = mid
    while i < n:
        right_array.append(array[i])
        i+=1

    MergeSort(left_array) 
    MergeSort(right_array)
    Merge(left_array, right_array, array)
    return array


#Main
random_numbers = []
for i in range(1000000):
    random_numbers.append(random.randint(0,i))
sorted_numbers = MergeSort(random_numbers)
#print sorted_numbers
