import random
import math


def feladat1(a: int, b: int):
    i: int = a
    osszeg: int = 0
    while i <= b:
        if i % 2 == 0:
            print(i)
            osszeg += i
        i += 1
    return osszeg


"""Írj függvényt amely generál 20 db random számot -10 és 10 között
számold meg hogy hánynegatív szám van benne
a visszatérési érték a negatív számok száma"""
def randomszamok():
    #i: int = 0
    mennyiseg: int = 0
    for i in range (0, 20, 1):
        szam:int = math.floor(random.random() * (10 + 1 -(-10)) + (-10))
        print(szam, end =", ")
        i += 1
        if szam < 0:
            mennyiseg += 1
    return mennyiseg


def feladat3(a: int, b:int):
    osszeg: int = 0
    for i in range (a, b, 1):
        if i % 2 == 0:
            print(i)
            osszeg += 1
    return osszeg


"""Írj függvényt amely generál 10 random számot 10 és 33 között és visszatér ezek összegével"""
def feladat4():
    osszeg: int = 0
    for i in range(0, 10, 1):
        szam:int = math.floor(random.random() * (34 - 12) + 12)
        print(szam, end = " ")
        osszeg += szam
        
    return osszeg

def feladat5():
    max:int = 0
    for i in range(0, 8, 1):
        szam:int = math.floor(random.random() * (51 - 20) + 20)
        print(szam, end = " ")
        if szam > max:
            max = szam

    return max

def feladat6():
    osszeg: int = 0
    for i in range(0, 3, 1):
        szam:int = int(input(f"Kérem az {i + 1}. egész számot: "))
        osszeg += szam
    return osszeg / 3

def feladat7():
    i:int = 0
    osszeg:int = 0
    db: int = 1
    szam:int = int(input(f"Kérem az {i + 1}. egész számot: "))
    while szam != 0:
        osszeg += szam
        db += 1
        szam:int = int(input(f"Kérem az {i + 1}. egész számot: "))
    
    return osszeg / (db - 1)
    

        
