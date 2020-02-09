def selection_sort(array):

    n = len(array)
    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if array[j]<array[min_index]:
                array[j],array[min_index] = array[min_index],array[j]
        


if __name__ == '__main__':
    
    array = [2,5,1,0,3,3]
    print(array)
    selection_sort(array)
    print(array)
    