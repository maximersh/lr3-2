n1 = float(input("Введите первое число: "))
n2= float(input("Введите второе число: "))
result = "Числа равны" if n1 == n2 else (f"Наименьшее число: {n1}" if n1 < n2 else f"Наименьшее число: {n2}")
print(result)