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
    vowels = set("aeiouAEIOU")

    def vowel_count(s: str) -> int:
        return sum(1 for c in s if c in vowels)

    def lexical_key(s: str):
        # Compare letters case-insensitively
        return tuple(c.lower() if c.isalpha() else c for c in s)

    return sorted(
        strings,
        key=lambda s: (
            len(s),
            lexical_key(s),
            vowel_count(s)
        )
    )


lst = ["zbdd", "abbc", "Jaa1  bb", "jaa2b  b"]
print(cryptic_sorter(lst))
