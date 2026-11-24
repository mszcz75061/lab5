# A. Wyświetlanie wartości parametrów
def wyswietl(*args):
    for wartosc in args:
        print(wartosc)

wyswietl(1, "kot", 3.5)

# B. Zwracanie wartości maksymalnej
def maksimum(*args):
    return max(args)

print("Maksimum:", maksimum(10, 25, 4, 99, 12))
