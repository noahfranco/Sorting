# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for smallest_index in range(cur_index + 1, len(arr)):
            if arr[smallest_index] < arr[cur_index]:
                arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]




    # TO-DO: swap
    return arr


print(selection_sort([1, 2, 3, 5, 4, 6, 8, 7, 9, 10]))
    

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr