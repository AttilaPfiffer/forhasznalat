import feladatok



negativ_db: int = feladatok.randomszamok()
print(f"A negatív számok száma: {negativ_db}")

for_szamok:int = feladatok.feladat3(0, 10)
print(f"Az összegük: {for_szamok}")

visszateres: int = feladatok.feladat4()
print(f"Az összegük: {visszateres}")

legnagyobb: int = feladatok.feladat5()
print(f"A legnagyobb szám: {legnagyobb}")

atlag: int = feladatok.feladat6()
print(f"A számok átlaga: {atlag}")

nullaig:int = feladatok.feladat7()
print(f"Ennek az átlaga: {nullaig}")