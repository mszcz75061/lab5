def oblicz_bmi(waga, wzrost):
    return waga / (wzrost ** 2)

waga = float(input("Podaj wagę w kg: "))
wzrost = float(input("Podaj wzrost w m: "))
bmi = oblicz_bmi(waga, wzrost)
print(f"Twoje BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Zakres: niedowaga")
elif bmi <= 24.9:
    print("Zakres: pożądana masa ciała")
elif bmi <= 29.9:
    print("Zakres: nadwaga")
elif bmi <= 34.9:
    print("Zakres: otyłość I stopnia")
elif bmi <= 39.9:
    print("Zakres: otyłość II stopnia")
else:
    print("Zakres: otyłość III stopnia")
