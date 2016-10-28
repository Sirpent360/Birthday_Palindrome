# перетворюємо список на число


def list_to_number(pal):
    output_palindrome = ""
    for dummy_sym in pal:
        output_palindrome += str(dummy_sym)
    return(output_palindrome)