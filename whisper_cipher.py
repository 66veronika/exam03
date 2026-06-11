# Write a function that creates a simple cipher by shifting letters in a st
# by a given amount. Non-alphabetic characters should remain unchanged.

def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    big_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in text:
        if char.isalpha():
            if char.islower():
                index = alphabet.index(char)
                new_index = (index + shift) % 26
                result += alphabet[new_index]
            elif char.isupper():
                index_up = big_alph.index(char)
                new_up_index = (index_up + shift) % 26
                result += big_alph[new_up_index]
        else:
            result += char
    return result


res = whisper_cipher("abBc1z", 2)
print(res)
