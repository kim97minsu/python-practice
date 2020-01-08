# Bubble Sort is a comparison sorting method 

def bubble_sort(arr):
    n = len(arr) - 1 
    swapped = True
    
    while(swapped):
        swapped = False
        # iterate through all array elements 
        for i in range(n):
            # compare one item to its neighbor
            if arr[i] > arr[i+1]:
                # if the first item is greater, swap it
                holder = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = holder
                swapped = True
    return arr

arr = [3,2,4,7,6,8,5,9,1]
bubble_sort(arr)
print(arr)
