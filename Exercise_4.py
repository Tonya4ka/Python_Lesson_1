# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
quadrant = int(input("Type a number of the quadrant: "))
if quadrant==1:
   print("x>0 and y>0")
elif quadrant==2:
   print("x<0 and y>0")
elif quadrant==3:
   print("x<0 and y<0")
elif quadrant==4:
   print("x>0 and y<0")
else:
   print("Wrong number, there are only 4 quadrants")