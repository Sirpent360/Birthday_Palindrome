"""
Проект Web Academy
Python for beginners
День народження (порахувати скільки днів прожив користувач, рахувати ювілеї або паліндроми)
Паліндроми (придумати варіанти паліндромів)
(паліндром - число яке читається однаково як зліва праворуч так зправа ліворуч)
(важливою якістю паліндрома є симметричність)
Зробити алгоритм генерації "золотих номерів" (як у мобільних операторів)
Вивести найближчі дати для цих паліндромів
---------------------------------------------
Варіанти паліндромів:
1) парний (1221, 123321)
2) непарний (12321, 23532)
3) однакова цифра (1111, 22222)

1) для парного - беремо n чисел(парне), додаємо n перевернутих цих же чисел (12, 12 => 21, 12 + 21 => 1221)
2) для непарного - беремо n чисел(парне), додаємо n перевернутих цих же чисел, між ними, "посередині", ще одне число,
отримуємо в результаті непарне число (12, 12 => 21, в центрі, наприклад 3, 12 + 3 + 21 => 12321)

"""
import datetime
from capot import list_to_number
from capot import list_to_number_int
from capot import number_to_list
from capot import lived_days
from capot import fake_palindrome
from palindrome import new_palindrome
from palindrome import new_center_next_palindrome
from gold_numbers import gold_3_in_row
from gold_numbers import gold_3_in_row_next

# Користувач вводить дату народження. Рік, місяць, день.

# birth_year = int(input("Введіть свій рік народження: "))
# birth_month = int(input("Введіть свій місяць народження: "))
# birth_day = int(input("Введіть свій день народження: "))
# #
# print()
# print("birth_year: ", birth_year)
# print("birth_month: ", birth_month)
# print("birth_day: ", birth_day)
# print()

# Вираховуємо кількість прожитих днів
#
# скільки днів прожито від дати народження до сьогоднішнього дня)

# today = datetime.date.today()
# print("Today is: ", today)
# # birth = datetime.date(birth_year, birth_month, birth_day)
birth = datetime.date(1977, 5, 30)
# lived = (abs(today - birth))
# print("You have already days lived: ", lived.days, "\n")

# Паліндром з кількості прожитих днів
#
# Отримуємо кількість прожитих днів
# Робимо з числа список
# робимо зі списку паліндром
# робимо з паліндрома(список) - паліндром (число)

dummy_palindrome = number_to_list(lived_days(birth))
print("dummy_palindrome is: ", dummy_palindrome)

lived = lived_days(birth)

# перетворюємо список на число
print("list_to_number palindrome ", list_to_number(new_palindrome(dummy_palindrome)[0]))
print("lived.days ", lived_days(birth))
delta = int(list_to_number(new_palindrome(dummy_palindrome)[0]))-lived_days(birth)
print("difference between lived_days(birth) and palindrome ", int(list_to_number(new_palindrome(dummy_palindrome)[0]))-lived_days(birth), "\n")

# перетворюємо список на число

new_center_palindrome = new_center_next_palindrome(new_palindrome(dummy_palindrome))
print("center_next_palindrome ", list_to_number([new_center_next_palindrome(dummy_palindrome)[0]]))     # new_center_next_palindrome
print("lived_days(birth) ", lived_days(birth))
delta2 = int(list_to_number([new_center_next_palindrome(dummy_palindrome)[0]]))-lived_days(birth)
print("difference between lived_days(birth) and center_next_palindrome ", int(list_to_number([new_center_next_palindrome(dummy_palindrome)[0]]))-lived_days(birth))


#   Календарні дати
# виводимо календарні дати, коли ці паліндроми будуть по календарю
# print("lived_days(birth) ", lived_days(birth))

today = datetime.date.today()
palindrome_date = today - datetime.timedelta(delta)
print()
print("date of next palindrome ", palindrome_date)
center_next_palindrome_date = today - datetime.timedelta(delta2)
print("date of another palindrome ", center_next_palindrome_date)
print()

#   Виведемо дати коли ці паліндроми відбувались у форматі: День Місяць Рік
# string_date =  my_date.strftime('%d/%m/%Y')  # This writes "24/06/1984"

# string_date_palindrome = palindrome_date.strftime('%d/%m/%Y')
# print("Your next palindrome date: ", string_date_palindrome, "\nYou will have days lived: ",
# list_to_number(palindrome))
print("Your next palindrome date: \nDay: %s Month: %s Year: %s" % (palindrome_date.day, palindrome_date.month, palindrome_date.year))
print("You will have days lived: ", list_to_number(new_palindrome(dummy_palindrome)[0]))
print()

# string_date_center_next_palindrome_date = center_next_palindrome_date.strftime('%d/%m/%Y')
# print("Your previous palindrome date: ", string_date_center_next_palindrome_date, "\nYou will has days lived: ",
# list_to_number(center_next_palindrome), "\n")
print("Your previous palindrome date: \nDay: %s Month: %s Year: %s" % (center_next_palindrome_date.day, center_next_palindrome_date.month, center_next_palindrome_date.year))
print("You has days lived: ", list_to_number(new_center_palindrome))
print()

# Виводимо золоті "номери"
# gold_3_in_row

delta3 = lived_days(birth) - (list_to_number_int(gold_3_in_row(new_palindrome(dummy_palindrome))))
print()
print("lived_days(birth): ", lived_days(birth))
print("dummy_palindrome: ", dummy_palindrome)
print("new_palindrome(dummy_palindrome): ", new_palindrome(dummy_palindrome))
# print("(new_palindrome(dummy_palindrome))[0]: ", (new_palindrome(dummy_palindrome))[0])
print("gold_3_in_row ",gold_3_in_row(new_palindrome(dummy_palindrome)))
print("list_to_number_int", list_to_number_int(gold_3_in_row(new_palindrome(dummy_palindrome))))
# print("int", int(list_to_number(gold_3_in_row(new_palindrome(dummy_palindrome)))))
print("delta3: ", delta3)
print()

print("Gold number: ", list_to_number_int(gold_3_in_row(new_palindrome(dummy_palindrome))))
gold_3_in_row_date = today - datetime.timedelta(delta3)
print("gold_3_in_row_date: ", gold_3_in_row_date, "\n")
# new_palindrome(dummy_palindrome)
print("Your previous gold number was: \nDay: %s Month: %s Year: %s" %
      (gold_3_in_row_date.day, gold_3_in_row_date.month, gold_3_in_row_date.year))
print("You has lived at previous gold number, days: ", list_to_number_int(gold_3_in_row(new_palindrome(dummy_palindrome))),"\n")

# gold_3_in_row_next

delta4 = lived_days(birth) - (list_to_number_int(gold_3_in_row_next(new_palindrome(dummy_palindrome))))
# delta3 = lived_days(birth) - (list_to_number_int(gold_3_in_row(new_palindrome(dummy_palindrome))))
gold_3_in_row_next_date = today - datetime.timedelta(delta4)
# new_palindrome(dummy_palindrome)
print("Your another gold number: \nDay: %s Month: %s Year: %s" %
      (gold_3_in_row_next_date.day, gold_3_in_row_next_date.month, gold_3_in_row_next_date.year))
print("You will have lived at another gold number, days: ", list_to_number_int(gold_3_in_row_next(new_palindrome(dummy_palindrome))),"\n")

# list_to_number(palindrome)
# list_to_number(center_next_palindrome)
# now = datetime.datetime.now()
# print("%s/%s/%s" % (now.day, now.month, now.year))
# palindrome_date
# print("Your next palindrome date: \nDay: %s Month: %s Year: %s" % (palindrome_date.day, palindrome_date.month,
# palindrome_date.year))

# наш внутрішній Unit-test )
if __name__ == "__main__":
    birth_year = 1977
    birth_month = 5
    birth_day = 30
    today = datetime.date(2016, 10, 29)
    # print("lived_days(birth) ", lived_days(birth))        # lived_days(birth) = 14396
    assert lived_days(birth) == 14397  # працює, видає AssertionError, якщо дати введена інша дата народження
