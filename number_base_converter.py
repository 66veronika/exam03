# Write a function that converts a number from one base to another.
# Support bases from 2 to 36 inclusive, using digits 0-9 and letters A-Z
# for values 10-35. Return "ERROR" for invalid inputs (base, digits)

def number_base_converter(number: str, from_base: int, to_base: int) -> str:

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    try:
        if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
            return "ERROR"
        num = int(number.upper(), from_base)

        if num == 0:
            return "0"

        result = ""

        while num:
            result += digits[num % to_base]
            num //= to_base

        return result[::-1]

    except ValueError:
        return "ERROR"


def main():
    print(number_base_converter("Ff", 16, 10))
    print(number_base_converter("00FF", 16, 2))
    print(number_base_converter("z", 36, 10))
    print(number_base_converter("1010", 2, 16))


if __name__ == "__main__":
    main()
