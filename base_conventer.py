#######################################################################
#  Given a string num representing a number in base `from_base`,      #
#  convert it to its representation in base `to_base` and return      #
#  the result as a string.                                            #
#                                                                     #
#  The function must:                                                 #
#       -> Support bases from 2 up to 36.                             #
#       -> Handle digits '0-9' and letters 'A-Z' (case-insensitive).  #
#       -> Preserve the correct value during conversion.              #
#       -> Return "0" if the input represents zero.                   #
#######################################################################

def convert_base(num: str, from_base: int, to_base: int) -> str:
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not num or num.strip() == "":
        return "ERROR"

    if not 2 <= from_base <= 36 or not 2 <= to_base <= 36:
        return "ERROR"

    num = num.upper()
    decimal_value = int(num, from_base)

    if decimal_value == 0:
        return "0"

    result = ""
    while decimal_value > 0:
        decimal_value, remainder = divmod(decimal_value, to_base)
        result = chars[remainder] + result

    return result


def main():
    print(convert_base("Ff", 16, 10))
    print(convert_base("00FF", 16, 2))
    print(convert_base("z", 36, 10))


if __name__ == "__main__":
    main()
