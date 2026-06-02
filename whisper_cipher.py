# Write a function that creates a simple cipher by shifting letters in a st
# by a given amount. Non-alphabetic characters should remain unchanged.

def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in text:
        if char.isalpha():
            index = alphabet.index(char)
            new_index = (index + shift) % 26
            result += alphabet[new_index]
        else:
            result += char
    return result


res = whisper_cipher("abc1z", 2)
print(res)
