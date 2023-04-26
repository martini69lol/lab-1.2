def b_sorter(array):
    length = len(array)
    for i in range(length):
        for j in range(0, length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


array_for_sort = [4, 1, 3, 2, 6, 5, 7]

print(b_sorter(array=array_for_sort))