def quickSort(arr, p, r):

    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q-1)
        quickSort(arr, q+1, r)


def partition(arr, p, r):

    x = arr[r]
    i = p-1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


if __name__ == '__main__':

    arr = [4, 6, 3, 7, 3, 7, 4]
    quickSort(arr, 0, 6)
    print(arr)
