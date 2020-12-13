def median(lst):
    lst.sort()
    print(lst)
    half = int((len(lst) - 1) / 2)
    print(half)
    print(lst[half])
    if len(lst) % 2 == 0:
        m = (lst[half] + lst[half + 1]) / 2
        return m
    else:
        m = lst[half]
        return m


print("median : ")
# stream = [9, 3, 4, 2, -1, -7, 5, -3]
# print(median(stream))

stream = [9, 3, 4, 2, -1, 5]
print(median(stream))