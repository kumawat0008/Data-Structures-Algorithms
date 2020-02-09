def isMaxHeap(arr, N):

    for i in range(int(N/2)):

        if arr[2*i+1] > arr[i] or arr[2*i+2] > arr[i]:
            return False

    return True


if __name__ == '__main__':

    arr = [0, 5, 3, 8, 2, 6, 7, 3, 5]
    print(isMaxHeap(arr, len(arr)))
