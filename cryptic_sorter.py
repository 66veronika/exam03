"""
Write a function that sorts a list of strings according to multiple criteria:
1. Primary sort: By string length (shortest first)
2. Secondary sort: ASCII order, except letters are compared case-insensitively
   (for strings of same length)
3. Tertiary sort: By number of vowels (ascending
for same length and lexically equal)
4. Equal strings will appear in the same order as in the input list.
"""


def swap_sort(arr1: str, arr2: str) -> bool:
    tmp_first = "".join(c1 for c1 in sorted(arr1))
    tmp_second = "".join(c2 for c2 in sorted(arr2))
    
    return tmp_first[0] < tmp_second[0]
        



def cryptic_sorter(strings: list[str]) -> list[str]:
    primary_sort = sorted(strings, key=lambda current: len(current))
    for i in range(len(primary_sort)):
        while i < len(primary_sort) - 1:
            if len(primary_sort[i]) == len(primary_sort[i + 1]):
                if swap_sort(primary_sort[i], primary_sort[i + 1]) != True:
                    primary_sort[i + 1], primary_sort[i] = primary_sort[i], 
                    primary_sort[i + 1]
               
            i += 1

    # print(primary_sort)

lst = ["zbdd", "abbc", "jaabb"]
print(cryptic_sorter(lst))