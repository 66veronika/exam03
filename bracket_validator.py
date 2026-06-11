# Write a function that checks if brackets [], parentheses (), and braces {}
# are properly balanced and correctly nested in a string. All others
# characters are ignored.Return True if balanced, False otherwise

def bracket_validator(s: str) -> bool:
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            if stack.pop() != pairs[char]:
                return False
    return len(stack) == 0
    #     if char in "([{":
    #         stack.append(char)
    #     elif stack[-1] == pairs[char]:
    #         stack.pop()
    #     else:
    #         return False

    # return not stack


print(bracket_validator("({{})"))
