a = [4, 1, 3, -9, 24, -64, 0, 0, 18, 11, -3]


def selected_sort(arr):
    for i in range(0, len(arr)):
        starting_index = i
        index_of_smallest = starting_index
        for j in range(i, len(arr)):
            if arr[j] < arr[index_of_smallest]:
                index_of_smallest = j
        arr[starting_index], arr[index_of_smallest] = arr[index_of_smallest], arr[starting_index]
    return arr


print(selected_sort(a))


# Start a function that takes in the array
#
#
#
#
#
#
#
#
#
#
