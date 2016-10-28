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

import time
#from datetime import date
import datetime

# перетворюємо список на число


def list_to_number(pal):
    output_palindrome = ""
    for dummy_sym in pal:
        output_palindrome += str(dummy_sym)
    return(output_palindrome)

birth_year = int(input("Введіть свій рік народження: "))
birth_month = int(input("Введіть свій місяць народження: "))
birth_day = int(input("Введіть свій день народження: "))
#
print()
print("birth_year: ", birth_year)
print("birth_month: ", birth_month)
print("birth_day: ", birth_day)
print()

    #
    #   Вираховуємо кількість прожитих днів
    #
    # скільки днів прожито від дати народження до сьогоднішнього дня
    #
today = datetime.date.today()
print("Today is: ", today)
birth = datetime.date(birth_year, birth_month, birth_day)
lived = (abs(today - birth))
print("You have already days lived: ", lived.days, "\n")


# 2016-10-03
# 14371 days, 0:00:00

# Паліндроми
# 14341



    #   Паліндром з кількості прожитих днів
    #
    #Отримуємо кількість прожитих днів
    #Робимо з числа список
    #робимо зі списку паліндром
    #робимо з паліндрома(список) - паліндром (число)
    #
    #

pal = str(lived.days)
dummy_palindrome = []
for dummy_x in pal:
    dummy_palindrome += [int(dummy_x)]
print("dummy_palindrome is: ", dummy_palindrome)

# якщо довжина паліндрома непарне число len(dummy_palindrome)
# first + center + end
#
# отримуємо новий паліндром через віддзеркалення "першої" частини


lenght = len(dummy_palindrome)
#print(lenght)
first_part_end_index = lenght // 2

first = dummy_palindrome[:first_part_end_index]
print("first ", first)

center_part_index = first_part_end_index
#print(center_part_index)
center = [dummy_palindrome[center_part_index]]
print("center ", center)

# # віддзеркалюємо першу половину - отримуємо

end = first[::-1]
print("end ", end)

palindrome = first + center + end
print("palindrome ", palindrome, "\n")

# перетворюємо список на число
print("list_to_number palindrome ", list_to_number(palindrome))
print("lived.days ", lived.days)
delta = int(list_to_number(palindrome))-lived.days
print("difference between lived.days and palindrome ", int(list_to_number(palindrome))-lived.days, "\n")

#
# отримуємо новий паліндром через зміну "центральної" частини
# додаємо одиницю до центральної частини - отримуємо
#
#

# змінюємо центральну частину

# a = [4]
# b = []
# b.append(a[0]+1)

center_next = []
center_next.append(center[0]+1)
print("center_next ", center_next)

# формуємо наступний паліндром з новою центральною частиною

center_next_palindrome = first + center_next + end
print("center_next_palindrome ", center_next_palindrome)

# перетворюємо список на число
print("center_next_palindrome ", list_to_number(center_next_palindrome))
print("lived.days ", lived.days)
delta2 = int(list_to_number(center_next_palindrome))-lived.days
print("difference between lived.days and center_next_palindrome ", int(list_to_number(center_next_palindrome))-lived.days)

#
#   Календарні дати
#
# друкуємо дати коли ці паліндроми будуть по календарю
#
#

# print("lived.days ", lived.days)

today = datetime.date.today()
palindrome_date = today - datetime.timedelta(delta)

print()
print("date of next palindrome ", palindrome_date)

center_next_palindrome_date = today - datetime.timedelta(delta2)

print("date of another palindrome ", center_next_palindrome_date)
print()

#
#
#   Виведемо дати коли ці паліндроми відбувались у форматі: День Місяць Рік
#
#

# string_date =  my_date.strftime('%d/%m/%Y')  # This writes "24/06/1984"

string_date_palindrome = palindrome_date.strftime('%d/%m/%Y')
# print("Your next palindrome date: ", string_date_palindrome, "\nYou will have days lived: ", list_to_number(palindrome))
print("Your next palindrome date: \nDay: %s Month: %s Year: %s" % (palindrome_date.day, palindrome_date.month, palindrome_date.year))
print("You will have days lived: ", list_to_number(palindrome))
print()

string_date_center_next_palindrome_date = center_next_palindrome_date.strftime('%d/%m/%Y')
# print("Your previous palindrome date: ", string_date_center_next_palindrome_date, "\nYou will has days lived: ", list_to_number(center_next_palindrome), "\n")
print("Your previous palindrome date: \nDay: %s Month: %s Year: %s" % (center_next_palindrome_date.day, center_next_palindrome_date.month, center_next_palindrome_date.year))
print("You has days lived: ", list_to_number(center_next_palindrome))
print()


# list_to_number(palindrome)
# list_to_number(center_next_palindrome)

# Друкуємо дати паліндромів у красивому вигляді
# День:  Місяць: Рік:
# now = datetime.datetime.now()
# >>> now.date()
# datetime.date(2016, 10, 25)
# >>> now.day
# 25
# >>> now.month
# 10
# >>> now.year
# 2016

# from datetime import datetime
# now = datetime.now()
#
# print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

# now = datetime.datetime.now()
# print("%s/%s/%s" % (now.day, now.month, now.year))
# palindrome_date

# print("Your next palindrome date: \nDay: %s Month: %s Year: %s" % (palindrome_date.day, palindrome_date.month, palindrome_date.year))