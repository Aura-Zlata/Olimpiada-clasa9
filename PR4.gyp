"""
Doi gospodari au loturi de aceiasi arie.
Un loc are forma patrata si este imprejmuit cu un gard de 48 m lungime.
Alt lot are forma unui dreptunghi cu latimea de 9 m.
Ce lungime are gardul care imprejmuieste acest loc?
"""

#lungime a gardului cu forma patrata
a=48
#lungimea laturii a patratului
c=48/4
#aria lui
d=c**2
#latime a lotului cu forma unui dreptunghi
b=9
#lungimea laturii a dreptunghiului
e=d/b
#lungime a gardului a dreptunghiului
f=(e+c)*2

print("Gardul care imprejmuieste acest loc are lungimea de",f,"metri.")
