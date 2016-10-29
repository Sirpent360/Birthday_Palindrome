from capot import list_to_number
from capot import list_to_number_int


# Генеруємо так звані золоті номери
# Наприклад 3 або 4 цифри підряд в кінці номера: 444, 333; 2222, 5555
# Або повторення 2 цифр в кінці номера: 01-01, 40-40


def gold_3_in_row(palindrome_list):         # palindrome_list = [palindrome, first, center, end]
    result = []
    result.append(int(str(palindrome_list[1][0])+str(palindrome_list[1][1])))
    # center_next.append(new_palindrome(dummy_palindrome)[2][0]+1)
    i = 0
    for i in range(3):
        result.append(palindrome_list[2][0])
        # Voodoo people magic people, беремо нульовий елемент списку, тобто його значення
    return result


def gold_3_in_row_next(palindrome_list):                        # palindrome_list = [palindrome, first, center, end]
    center_next = []
    center_next.append(palindrome_list[2][0] + 1)
    result = []
    result.append(int(str(palindrome_list[1][0])+str(palindrome_list[1][1])))
    # center_next.append(new_palindrome(dummy_palindrome)[2][0]+1)
    i = 0
    for i in range(3):
        result.append(list_to_number_int(center_next))
    return result


# print(gold_3_in_row([[1, 4, 3, 4, 1], [1, 4], [3], [4, 1]]))    # palindrome_list = [palindrome, first, center, end]
# print(gold_3_in_row_next([[1, 4, 3, 4, 1], [1, 4], [3], [4, 1]]))

if __name__ == "__main__":
    palindrome_list = [[1, 4, 3, 4, 1], [1, 4], [3], [4, 1]]
    assert gold_3_in_row(palindrome_list) == [14, 3, 3, 3]
    palindrome_list = [[1, 4, 3, 4, 1], [1, 4], [3], [4, 1]]
    assert gold_3_in_row_next(palindrome_list) == [14, 4, 4, 4]
