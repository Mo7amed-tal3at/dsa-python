
def counting_sort(arr: list[int]) -> list[int]:
    if not arr :
        return arr
    maximum = max(arr)
    count = [0]*(maximum+1)
    for i in arr:
        count[i]+=1
    result = []
    for i, freq in enumerate(count):       
        result += [i] * freq

    return result


def counting_sort_by_digit(arr: list[int], place: int) -> list[int]:
    buckets = [[] for _ in range(10)]
    for num in arr :
        digit = (num//place)%10
        buckets[digit].append(num)
    result=[]
    for bucket in buckets:
        result += bucket
    return result         