def find_all_subarrays_with_sum_k(array,sum):
    map = dict()
    curr_sum = 0

    for i in range(len(array)):
        curr_sum+=array[i]

        if curr_sum == sum:
            return (0,i)
        
        if curr_sum-sum in map:
            return (map[curr_sum-sum]+1,i)

        map[curr_sum] = i

    return (-1,-1)

if __name__ == '__main__': 

    arr = [10, 2, -2, -20, 10]  
    result = find_all_subarrays_with_sum_k(arr,-10) 
    print(result)


