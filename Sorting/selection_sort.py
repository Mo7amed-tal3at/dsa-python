def selection_sort(arr: list[int]):
    for i in range(len(arr)):
        min_idx = i 
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                min_idx= j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr