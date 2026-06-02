# Write a function that merges two sorted lists into one sorted list.

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    return sorted(list1 + list2)


list1 = [0, 3, 5]
list2 = [2, 6, 7]

res = shadow_merge(list1, list2)
print(res)