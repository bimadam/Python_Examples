import os
import time

#os.name
print(os.name)

print ("")

#zobrazení aktuálního pracovního adresáře
cwd = os.getcwd()
print ("Aktuální pracovní adresář:", cwd)

#změna aktuálního pracovního adresáře
os.chdir ('../')
chwd = os.getcwd()
print ("Změněný pracovní adresář: ", chwd)

print ("")

#vytváření nového adresáře
path = "C:\AHOJ"
os.mkdir(path)
print ("Adresář", path, "byl vytvořen.")

print ("")

#zobrazení souborů a adresářů
path2 = "C:\Windows"
list = os.listdir(path2)
print ("Soubory a adresáře v", path2, ":", list)

print ("")

#vytvoření souboru
os.chdir ('C:\AHOJ')
open ("text.txt", "x")
file = "text.txt"
print ("Soubor", file, "byl vytvořen.")

#přejmenování souboru
os.rename(file, 'ahoj.txt')
file2 = "ahoj.txt"
print ("Soubor", file, "byl přejmenován na", file2)

#zobrazení velikosti souboru
size = os.path.getsize("ahoj.txt")
print ("Velikost souboru", file2, "je", size, "bytů.")

time.sleep(5)

print ("")

#mazání souborů
os.remove(file2)
print ("Soubor", file2, "byl smazán.")

time.sleep(1.5)

print ("")

#mazání adresářů
os.chdir ('../')
os.rmdir (path)
print ("Adresář", path, "byl smazán.")