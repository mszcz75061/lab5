import math

def pole_trojkata(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Boki muszą być większe od zera.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Z podanych boków nie da się zbudować trójkąta.")
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

try:
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    c = float(input("Podaj bok c: "))
    print("Pole trójkąta:", pole_trojkata(a, b, c))
except ValueError as e:
    print("Błąd:", e)
