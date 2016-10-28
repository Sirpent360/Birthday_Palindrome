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

if __name__ == "__main__":
    pal = [1, 4, 3, 9, 6]
    assert list_to_number(pal) == 14396
    number = 14396
    assert number_to_list(number) == [1, 4, 3, 9, 6]