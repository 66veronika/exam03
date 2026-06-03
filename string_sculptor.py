# Write a function that transforms a string by alternating the case of
# alphabetic characters only. Non-alphabetic characters (spaces, digits,
# punctuation) stay as they are and do not advance the alternation counter.
# The first alphabetic character should be lowercase, the second uppercase,
# the third lowercase, and so on.

def string_sculptor(text: str) -> str:
    res = ""
    count = 0

    for char in text:
        if char.isalpha():
            if count % 2 == 0:
                res += char.lower()
            elif count % 2 != 0:
                res += char.upper()
            count += 1
        else:
            res += char
    return res


print(string_sculptor("a1bc4aa"))
