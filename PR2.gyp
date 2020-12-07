"""
Trei purcei au impartit frateste n alune, cele ramase le au dat Ritei.
Realizati un program care, citind de la tastatura numarul de alune, sa se afiseze la ecran cate alune au revenit fiecarui purcel si cate alune au ramas pentru Rita?
Exemplu:
Date de intrare: nr. de alune 86.
Date de iesire: pentru fiecare purcel revine 28 alune, Ritei 1- au ramas 2 alune.
"""

n=eval(input("Introduceti numarul de alune: "))
print("Fiecarui purcelus ii revine",n//3,"alune, iar Ritei ii raman",n%3,"alune.")
