def mergesort(arr):

    if len(arr) > 1:

        # Divide left and right subarray
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call of left and right
        mergesort(left)
        mergesort(right)

        
        lIndex = rIndex = index = 0
        
        # Merging left and right subarrays
        while lIndex < len(left) and rIndex < len(right):

            if left[lIndex] <= right[rIndex]:
                arr[index] = left[lIndex]
                lIndex += 1
                index += 1
            else:
                arr[index] = right[rIndex]
                rIndex += 1
                index += 1

        # Adding the extra elements left in the subarrays
        while lIndex < len(left):
            
            arr[index] = left[lIndex]
            lIndex += 1
            index += 1
            
        while rIndex < len(right):
            
            arr[index] = right[rIndex]
            rIndex += 1
            index += 1


if __name__ == "__main__":

    arr = list(map(int, input().split()))
    mergesort(arr)
    print(arr)
    
    
