# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример: - 6 -> да
# - 7 -> да
# - 1 -> нет
number = int(input("Type a week day number: "))
if number>=1 and number<=5:
   print("No")
elif number==6 or number==7:
   print("Yes")
else:
   print("Wrong number")