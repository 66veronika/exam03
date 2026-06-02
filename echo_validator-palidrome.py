# Write a function that checks if a string is a palindrome, ignoring spaces
# and case, only consider alphabetic characters for the comparison. The funct

def echo_validator(text: str) -> bool:
    cleaned = ""

    for char in text:
        if char.isalpha():
            cleaned += char.lower()

    return cleaned == cleaned[::-1]


res = echo_validator("ababa")
print(res)
