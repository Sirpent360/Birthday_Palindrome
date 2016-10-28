

def list_to_number(pal):        # перетворюємо список на число(строку)
    output_palindrome = ""
    for dummy_sym in pal:
        output_palindrome += str(dummy_sym)
    return output_palindrome


def number_to_list(number):     # перетворюємо число на список
    dummy_palindrome = []
    for dummy_x in str(number):
        dummy_palindrome += [int(dummy_x)]
    return dummy_palindrome


if __name__ == "__main__":
    pal = [1, 4, 3, 9, 6]
    assert list_to_number(pal) == "14396"
    number = 14396
    assert number_to_list(number) == [1, 4, 3, 9, 6]