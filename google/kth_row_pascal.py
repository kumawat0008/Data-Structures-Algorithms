def kth_row(k):
    
    pre_array = [1]

    if k==1:
        return pre_array

    for i in range(2,k+1):
        array = [0]*i
        array[0]=array[-1] = 1
        for j in range(1,i-1):
            array[j] = pre_array[j]+pre_array[j-1]
        pre_array = array
        
    
    return array


if __name__ == '__main__':
    k = int(input())
    print(kth_row(k+1))