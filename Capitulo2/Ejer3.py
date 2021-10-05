num = int(input("Ingrese un num: "))

if 0 < num < 13:
    print("Es un nine")
elif 13 <= num <= 18:
    print("Es un adolescent")
elif 18 < num <= 60:
    print("Adult")
elif num>60:
    print("Esta viejo")
