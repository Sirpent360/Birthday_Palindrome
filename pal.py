from time import dummy_palindrome


def new_palindrome(dummy_palindrome):
    # якщо довжина паліндрома непарне число len(dummy_palindrome)
    # first + center + end
    #
    # отримуємо новий паліндром через віддзеркалення "першої" частини
    lenght = len(dummy_palindrome)
    # print(lenght)
    first_part_end_index = lenght // 2
    first = dummy_palindrome[:first_part_end_index]
    # print("first ", first)
    center_part_index = first_part_end_index
    # print(center_part_index)
    center = [dummy_palindrome[center_part_index]]
    # print("center ", center)
    # # віддзеркалюємо першу половину - отримуємо
    end = first[::-1]
    # print("end ", end)
    palindrome = first + center + end
    # print("palindrome ", palindrome, "\n")
    palindrome_list = [palindrome, first, center, end]
    # print("palindrome_list ", palindrome_list, "\n")
    return palindrome_list


def new_center_next_palindrome(palindrome_list):
    # отримуємо новий паліндром через зміну "центральної" частини
    # додаємо одиницю до центральної частини - отримуємо
    # змінюємо центральну частину
    # a = [4]
    # b = []
    # b.append(a[0]+1)
    center_next = []
    center_next.append(new_palindrome(dummy_palindrome)[2][0]+1)
    # print("center_next ", center_next)
    # формуємо наступний паліндром з новою центральною частиною
    # center_next_palindrome = new_palindrome(dummy_palindrome)[1] + center_next + new_palindrome(dummy_palindrome)[3]
    result = new_palindrome(dummy_palindrome)[1] + center_next + new_palindrome(dummy_palindrome)[3]
    # print("center_next_palindrome ", result)
    return result