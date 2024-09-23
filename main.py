import math

x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = float(input("Введите z: "))
if z < 1 and z > -1:
    B = math.sqrt(10 * (x * (1. / 3.) + x * (y + 2))) * ((math.asin(z) ** 2) - abs(x - y))
    print(B)
else:
    print("Введите корректные значения, так как z всегда должен быть от -1 до 1")