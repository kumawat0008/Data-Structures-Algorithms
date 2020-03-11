def findWater(arr, n): 
  
    left = [0]*n 
  
    right = [0]*n 
  
    water = 0
  
    left_max = arr[0]
    for i in range( 1, n): 
        
        left[i] = left_max
        if arr[i]>left_max:
            left_max = arr[i]
  
    right_max = arr[-1]
    for i in range(n-2, -1, -1): 
        right[i] = right_max
        if arr[i]>right_max:
            right_max = arr[i] 

    for i in range(1, n-1): 
        minimum= min(left[i], right[i])
        if minimum-arr[i]<0:
            pass
        else:
            water+=minimum-arr[i]
  
    return water 
    
arr = [3,0,4,2,0,4] 
n = len(arr) 
print(findWater(arr, n)) 