import sys
dp = {}
def get_max(arr, n):
    if n == 2:
        max_val = max(arr)
        return max_val
    if n == 1:
        return arr[0]
    if n == 0:
        return 0
    maxx = -sys.maxsize+1
    new_arr = []
    sub_arr_string = ''
    for i in arr:
        sub_arr_string +=str(i)
    if sub_arr_string not in dp:
        for i in range(len(arr)):
            taken = arr[i]
            if i == 0:
                new_arr = []
                for j,ele in enumerate(arr):
                    if j ==0 or j ==1:
                        pass
                    else:
                        new_arr.append(ele)
            elif i == n-1:
                new_arr = []
                for j,ele in enumerate(arr):
                    if j ==n-1 or j ==n-2:
                        pass
                    else:
                        new_arr.append(ele)
            else:
                new_arr = []
                for j,ele in enumerate(arr):
                    if j == i or j ==i-1 or j ==i+1:
                        pass
                    else:
                        new_arr.append(ele)
                
            val = taken+get_max(new_arr,len(new_arr))
            if val>maxx:
                maxx = val
        dp[sub_arr_string] = maxx
    return dp[sub_arr_string]



arr = [-2,1,3,-4,5]

print(get_max(arr,len(arr)))