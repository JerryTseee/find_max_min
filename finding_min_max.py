def find_min_max(arr):
    n = len(arr)
    #if the length is even
    if n % 2 == 0:
        if arr[0] < arr[1]:
            min_val = arr[0]
            max_val = arr[1]
        else:
            min_val = arr[1]
            max_val = arr[0]
        index = 2
    #if the length is odd
    else:
        min_val = arr[0]
        max_val = arr[0]
        index = 1

    #comparing the remaining parts
    while index < n-1:
        if arr[index] < arr[index+1]:
            if arr[index] < min_val:
                min_val = arr[index]
            if arr[index + 1] > max_val:
                max_val = arr[index + 1]
        else:
            if arr[index] > max_val:
                max_val = arr[index]
            if arr[index + 1] < min_val:
                min_val = arr[index + 1]
        index += 2
    
    #return results
    return min_val, max_val

arr = [5, 3, 8, 2, 9, 1, 6, 4]
min_val, max_val = find_min_max(arr)
print("Minimum:", min_val)
print("Maximum:", max_val)