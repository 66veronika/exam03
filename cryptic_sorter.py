"""
Write a function that sorts a list of strings according to multiple criteria:
1. Primary sort: By string length (shortest first)
2. Secondary sort: ASCII order, except letters are compared case-insensitively
   (for strings of same length)
3. Tertiary sort: By number of vowels (ascending
for same length and lexically equal)
4. Equal strings will appear in the same order as in the input list.
"""


def cryptic_sorter(strings: list[str]) -> list[str]:

    def vowel_count(s: str) -> int:
        vowels = "aeiouAEIOU"
        count = 0
        for c in s:
            if c in vowels:
                count += 1
        return count

    return sorted(
        strings,
        key=lambda text: (
            len(text),
            text.lower(),
            vowel_count(text)
        )
    )


lst = ["zbdd", "abbc", "Jaa1  bb", "jaa2b  b"]
print(cryptic_sorter(lst))
