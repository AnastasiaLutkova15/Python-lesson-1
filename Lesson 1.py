# Task 2

n = int(input("Введите трехзначное число: "))
a = n % 10
b = n % 100 // 10
c = n // 100
print("Сумма цифр:", a + b + c)

# Task 4

# s = int(input("Общее кол-во журавликов: "))
# petya = int(s / 6)
# serg = int(petya)
# katya = int((serg + petya) * 2)
# print(petya, katya, serg)

# Task 6

# n = int(input("Номер билета: "))
# a = n // 1000
# b = n % 1000
# num1 = a // 100
# num2 = a % 100 // 10
# num3 = a % 10
# sum1 = num1 + num2 + num3
# num4 = b // 100
# num5 = b % 100 // 10
# num6 = b % 10
# sum2 = num4 + num5 + num6
# if sum1 == sum2:
#     print("yes")
# else:
#     print("no")

# Task 8

# n = int(input("Кол-во долек шоколадки в длину: "))
# m = int(input("Кол-во долек шоколадки в ширину: "))
# k = int(input("Кол-во долек, которое нужно отломить: "))
# if n*m>k:
#     if k % n == 0 or k % m == 0:
#         print("yes")
#     else:
#         print("no")
# else:
#     print("no")

