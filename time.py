import datetime
from capot import number_to_list

birth = datetime.date(1977, 5, 30)


def lived_days(birth):
    today = datetime.date.today()
    lived = (abs(today - birth))
    return lived.days


def dummy_palindrome(lived_days):
    result = number_to_list(lived_days)
    return result


# today = datetime.date.today()
# print("Today is: ", today)
# # birth = datetime.date(birth_year, birth_month, birth_day)
# birth = datetime.date(1977, 5, 30)
# lived = (abs(today - birth))
# print("You have already days lived: ", lived.days, "\n")

# Паліндром з кількості прожитих днів
#
# Отримуємо кількість прожитих днів
# Робимо з числа список
# робимо зі списку паліндром
# робимо з паліндрома(список) - паліндром (число)

# dummy_palindrome = number_to_list(lived.days)
# print("dummy_palindrome is: ", dummy_palindrome)

print("lived.days: ", lived_days(birth))
print("dummy_palindrome: ", dummy_palindrome(lived_days(birth)))