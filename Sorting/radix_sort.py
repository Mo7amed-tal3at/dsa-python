from counting_sort import counting_sort_by_digit

def radix_sort(arr: list[int]) -> list[int]:
    max_val = max(arr)
    place = 1
    while max_val // place > 0:  
        arr = counting_sort_by_digit(arr, place)
        place *= 10 
    return arr