# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
# Пример: - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
x = int(input("Type a coordinate of x: "))
y = int(input("Type a coordinate of y: "))
if x>0 and y>0:
   print("1-st quadrant")
elif x>0 and y<0:
   print("4-th quadrant")
elif x<0 and y>0:
   print("2-nd quadrant")
elif x<0 and y<0:
   print("3-rd quadrant")
else:
   print("x or y could not be equal to zero")