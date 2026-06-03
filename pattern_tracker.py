# Write a function that counts the number of valid consecutive digit pairs in a
# string. A valid pair consists of two adjacent digits where the second digitis
# exactly one greater than the first digit. A 9 followed by a 0 is NOT a valid
# pair and only consider consecutive characters that are both digits (0-9).

def pattern_tracker(text: str) -> int:
    count = 0
    for i in range(len(text) - 1):
        if text[i].isdigit() and text[i + 1].isdigit():
            if int(text[i]) + 1 == int(text[i + 1]):
                count += 1
    return count


print(pattern_tracker("a1b23456"))
