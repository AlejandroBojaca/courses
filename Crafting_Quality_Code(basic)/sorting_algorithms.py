# Bubble sort

def bubble_sort(array):
    # array<num>
    end = len(array) - 1
    while end > 0:
        for i in range(end):
            if array[i] > array [i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]
        end -= 1
    return array

def selection_sort(array):
    # array<num>
    size = len(array)
    pointer = 0
    while pointer != size:
        min_index = pointer
        for i in range(pointer + 1, size):
            if array[i] < array[min_index]:
                min_index = i
        array[pointer], array[min_index] = array[min_index], array[pointer]
        pointer += 1
    return array

def insertion_sort(array):
    #array<num>
    size = len(array) - 1
    for i in range(1, size):
        if array[i] > array[i+1]:
            j = i + 1
            while j != 0 and array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]     
                j -= 1    
    return array


print(insertion_sort([2,3,4,5,1,3,2]))
