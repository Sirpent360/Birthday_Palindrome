# перетворюємо список на число


def list_to_number(pal):
    output_palindrome = ""
    for dummy_sym in pal:
        output_palindrome += str(dummy_sym)
    return output_palindrome

# перетворюємо число на список


def number_to_list(number):
    dummy_palindrome = []
    for dummy_x in str(number):
        dummy_palindrome += [int(dummy_x)]
    return dummy_palindrome
