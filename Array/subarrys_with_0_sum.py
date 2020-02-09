def find_all_subarrays_with_zero_sum(array):
    sum =0
    result = []
    map = dict()

    for i in range(len(array)):
        sum+=array[i]

        if sum == 0:
            result.append((0,i))
        
        if sum in map:
            for index in map[sum]:
                result.append((index+1,i))

        try:
            map[sum].append(i)
        except:
            map[sum] = [i]

    return result

if __name__ == '__main__': 

    arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7] 
    result = find_all_subarrays_with_zero_sum(arr) 
    print(result)


