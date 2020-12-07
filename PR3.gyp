"""
Sa se scrie un program care citeste un numar de ani si calculeaza numarul de luni, zile si ore corespunzatoare.
Se considera ca un an are 365 zile.
Exemplu:
Date de intrare: 2
Date de iesire: 24 luni  730 zile   17520 ore.
"""

n=eval(input("Introduceti ani: "))
print(n*12,"luni ",n*365,"zile ",n*365*24,"ore")
