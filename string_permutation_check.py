# Write a function that determines if two strings are permutations of each
# other. Two strings are permutations if they contain the same characters with
# the same frequencies.

def string_permutation_checker(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return (sorted(s1) == sorted(s2))


print(string_permutation_checker("he llo", "elloh "))
