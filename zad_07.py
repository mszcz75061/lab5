def potega(a, n):
    if n == 0:
        return 1
    return a * potega(a, n - 1)

a = float(input("Podaj podstawę a: "))
n = int(input("Podaj wykładnik n (całkowity >= 0): "))
print("Wynik:", potega(a, n))
