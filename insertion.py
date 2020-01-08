def insertion_sort(arr):
    # iterate over the given array
    for i in range(1, len(arr)):
        current = arr[i]
        position = i 
        
        while position > 0 and arr[position-1] > current:
            print("Swapped {} for {}".format(arr[position], arr[position-1]))
            arr[position] = arr[position-1] 
            print(arr)
            position -= 1 
            
        arr[position] = current 
    return arr
        
arr = [12, 3, 7, 4, 120, 20, 43, 51, 1]

print(insertion_sort(arr))