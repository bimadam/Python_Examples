#Created by Adam Bím
#01/2022

import time

zacatek = ("""
Skript pro výpočet bitového posuvu
""")
print (zacatek)

time.sleep (1.5)

hodnota = int(input("Zadej hodnotu: "))
posun = int(input("O kolik chceš číslo posunout?: "))
smer = input("A jakým směrem chceš posunout? (doleva, doprava): ")
vysledek = 0


if hodnota <= 0:
    quit ("Zadal jsi zápornou hodnotu!")

if posun <= 0:
    quit ("Zadal jsi záporný posun!")

if smer == 'doleva':
    vysledek = hodnota << posun

if smer == 'doprava':
    vysledek = hodnota >> posun 

print ("Zadaná hodnota byla:", hodnota, ".\nVýsledek je:", vysledek)

hodnota_bin = bin (hodnota)
posun_bin = bin (posun)

print ("\nZadaná hodnota v dvojkové číselné soustavě je", hodnota_bin, ".\nPosun v dvojkové číselné soustavě je", posun_bin)