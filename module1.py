from MyMoodle import *

failide_kustutamine()

ümber_kirjuta_fail(input("Faili nimi: "))

kirjuta_failisse("kasutajad.txt","salasõnad.txt")

päevad=loe_faelist("paevad.txt")

print(päevad)
for päev in päevad:
    print(päev)

