"""
La o ferma avicola sunt x pasari.
Jumatate din acestea sunt gaini.
Numarul ratelor constituie un sfert din numarul gainilor.
Scrieti un program care citeste de la tastatura numarul total de gaini, rate si gaste.
Exemplu: 
Date de intrare: 4560 - pasari
Date de iesire: gaini - 2280, rate - 570, gaste - 1710.
"""

p=eval(input("Introduceti nr total de pasari: "))
print("gaini - ",p//2,", rate - ",(p//2)//4,", gaste - ",p-(((p//2)//4)+p//2)) 