# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример: - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
x_a = float(input("Type x-coordinate of the point A: "))
y_a = float(input("Type y-coordinate of the point A: "))
x_b = float(input("Type x-coordinate of the point B: "))
y_b = float(input("Type y-coordinate of the point B: "))
d = ((x_b-x_a)**2+(y_b-y_a)**2)**0.5
print(round(d,2))