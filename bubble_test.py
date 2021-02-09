from main import quicksort
from main import matrix, row

def bubble_sort(lst):
    for num in range(len(lst) - 1, 0, -1):
        for item in range(num):
            if lst[item] > lst[item + 1]:
                lst[item], lst[item + 1] = lst[item + 1], lst[item]

    return lst


for i in range(row):
    print(bubble_sort(matrix[i]))
print()
for i in range(row):
    print(quicksort(matrix[i]))