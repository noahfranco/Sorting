# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arra, arrb):
    elements = len(arra) + len(arrb)
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    for i in range(0, elements):

        if a >= len(arra): # if there are no more elements in left side
            merged_arr[i] = arrb[b] # merge from the right side
            b += 1 # increment index for right side
        elif b >= len(arrb): # if no elements in right side
            merged_arr[i] = arra[a] # merge from the left side
            a += 1 # increment index for left side
        elif arra[a] < arrb[b]: # check first element of each list to see which one is greater
            merged_arr[i] = arra[a]
            a += 1
        else:
            merged_arr[i] = arrb[b]
            b += 1



    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # base case
    if len(arr) > 1: # if length of the list !> 1, return list
        middle = len(arr) // 2 # find middle list
        # Split list in halves
        first_half = arr[0: middle]
        second_half = arr[middle:]
        # Recursively split each half
        arra = merge_sort(first_half)
        arrb = merge_sort(second_half)
        # call Merge( with both halves
        arr = merge(arra, arrb)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
