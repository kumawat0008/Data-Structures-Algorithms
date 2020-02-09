def isMaxHeap(arr, i, N):

    if i >= int(N/2):
        return True

    left_child = isMaxHeap(arr, (2*i+1), N)
    right_child = isMaxHeap(arr, (2*i+2), N)

    if arr[i] >= arr[2*i+1] and arr[i] >= arr[2*i+1] and left_child and right_child:
        return True

    else:
        return False


if __name__ == '__main__':

    arr = [0, 5, 3, 8, 2, 6, 7, 3, 5]
    print(isMaxHeap(arr, 0, len(arr)))
