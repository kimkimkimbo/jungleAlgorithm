#배열을 더 이상 쪼갤 수 없을 때까지 쪼개서 분할해서 정렬


arr1 = [2,1,5,6,7,3,4]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    
    left = [x for x in arr[1:] if pivot > x]
    right = [x for x in arr[1:] if pivot <= x ]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

    
print(quick_sort(arr1))