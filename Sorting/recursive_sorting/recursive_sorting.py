def merge(arrA, arrB):

    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # [0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0]
    a = 0
    b = 0
    for i in range(0, elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        elif arrB[b] <= arrA[a]:
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


THIS_IS_A_VARIABLE = 928374928374

[-1, 4, 6, 7, 8]
[-7, -4, 0, 3, 3, 7]

# TO-DO
# Make two variables that are TRACKERS of where I am in each array.
# a=0
# b=0
# Create a for loop that iterates over the merged_arr for the entire length (i will be index number of merged arr).
# Create IF STATEMENTS!
# If When b tracker gets to be larger than the length of the array b, I want to add the a element
# Add the element from the a array that we are looking with the a tracker
# increment the a tracker a += 1
# Elif When a tracker gets to be larger than the length of the array a, I want to add the b element
# Add the element from the b array that we are looking with the b tracker
# increment the a tracker b += 1
# Elif statement that if arrA[a] < arrB[b] than:
# then merged_arr[i] will be set equal to arrA[a]
# increment tracker a   a +=1
# Elif statement that if arrB[b] <= arrA[a] than:
# then merged_arr[i] will be set equal to arrB[b]
# increment tracker b   b +=1
# Return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
test_array = [8, 1, 4, 6, 5, 3]


def merge_sort(arr):
    # TO-DO
    print(arr)
    # [8,1,4,6,5,3]
    if len(arr) <= 1:
        return arr
    halfway_point = len(arr) // 2
    print(arr[:halfway_point])  # [8,1,4]
    left = [1, 4, 8]

    print(arr[halfway_point:])
    right = [3, 5, 6]

    def merge(arrA, arrB):
        elements = len(arrA) + len(arrB)
        merged_arr = [0] * elements
        # [0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0]
        a = 0
        b = 0
        for i in range(0, elements):
            if a >= len(arrA):
                merged_arr[i] = arrB[b]
                b += 1
            elif b >= len(arrB):
                merged_arr[i] = arrA[a]
                a += 1
            elif arrA[a] < arrB[b]:
                merged_arr[i] = arrA[a]
                a += 1
            elif arrB[b] <= arrA[a]:
                merged_arr[i] = arrB[b]
                b += 1
        return merged_arr

    sorted_array = merge(left, right)
    print(sorted_array)
    return sorted_array


print([1, 3, 4, 5, 6, 8, ])

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
