# Write a function that checks if a string is a palindrome, ignoring spaces
# and case, only consider alphabetic characters for the comparison. The funct

def echo_validator(text: str) -> bool:
    new_str = "".join(c for c in text if c.isalnum()).lower()
    return new_str[::-1] == new_str


res = echo_validator("ababa")
print(res)
