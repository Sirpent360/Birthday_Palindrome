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
from capot import number_to_list
from project_birthday_palindrome import new_palindrome
from project_birthday_palindrome import center_next_palindrome


birth_year = int(input("Введіть свій рік народження: "))
birth_month = int(input("Введіть свій місяць народження: "))
birth_day = int(input("Введіть свій день народження: "))

    #   Вираховуємо кількість прожитих днів
    #
    # (скільки днів прожито від дати народження до сьогоднішнього дня)

today = datetime.date.today()
print("Today is: ", today)
birth = datetime.date(birth_year, birth_month, birth_day)
lived = (abs(today - birth))
print("You have already days lived: ", lived.days, "\n")

dummy_palindrome = number_to_list(lived.days)


if __name__ == "__main__":
    birth_year = 1977
    birth_month = 5
    birth_day = 30
    today = datetime.date(2016, 10, 28)
    assert lived.days == 14396              # працює, видає AssertionError, якщо дати введена інша дата народження