def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1 :
        return arr
    pivot = arr[-1]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)