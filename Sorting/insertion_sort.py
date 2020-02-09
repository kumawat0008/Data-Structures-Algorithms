def insertion_sort(array):
    
    n = len(array)
    for i in range(1,n):
        key = array[i]

        j = i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j-=1

        array[j+1] = key
            




if __name__ == '__main__':
    
    array = [2,5,1,0,8,3]
    print(array)
    insertion_sort(array)
    print(array)
    