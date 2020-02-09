def bubble_sort(array):
    
    n = len(array)
    for i in range(n):
       
        for j in range(0,n-i-1):

            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]


if __name__ == '__main__':
    
    array = [2,5,1,0,8,3]
    print(array)
    bubble_sort(array)
    print(array)
    