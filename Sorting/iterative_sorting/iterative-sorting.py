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
#   Set a flag that will be False until the array has been run through start to finish without changing anything.
#   Create a While loop that runs while the flag is False.
#       Set the flag to True (if it is not set to False later on, this will be the last iteration).
#       Set a For loop that runs through the array indexes except for the last one.
#           If the index being looked at is greater than the index one higher:
#               Switch the current index value with the value of the index one higher.
#               Set the flag to False.
#               Keep going.
#   Being out of the While loop means we have run through the array with anything being changed.
#   This means it should be sorted.
#   Return the array.


def bubble_sort(arr):
    flag = True
    while flag == True:
        flag = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = True
    return arr


print(bubble_sort(a))

