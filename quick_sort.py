def quick_sort(l):
    if len(l) == 0:
        return l
    pivot = l[0]
    pivots = [x for x in l if x == pivot]
    smaller = quick_sort([x for x in l if x < pivot])
    larger = quick_sort([x for x in l if x > pivot])
    return smaller + pivots + larger
array = [12, 4, 5, 6, 7, 3, 1, 15, 17]
print(quick_sort(array))
