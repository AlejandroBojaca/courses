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
    size = len(array)
    for i in range(1, size):
        if array[i] < array[i-1]:
            j = i
            while j != 0 and array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]     
                j -= 1    
    return array

monthly_profits = [0.0753761503, 1.896181661, 9.358328301, 1.258097247, 0.1934338566, 1.614021654, 1.415557906, 0.4779822076]

# Calculate Cumulative Profits
cumulative_profits = [monthly_profits[0]]
for profit in monthly_profits[1:]:
    cumulative_profits.append(cumulative_profits[-1] + profit)

print(cumulative_profits)

# Calculate Annual CAGR
beginning_value = monthly_profits[0]
ending_value = cumulative_profits[-1]
n = len(monthly_profits)
total_years = n / 12  # Assuming each value represents a monthly profit

annual_cagr = (ending_value / beginning_value) ** (1 / total_years) - 1

# print('Annual CAGR:', annual_cagr)

# print(insertion_sort([3,2,1]))
