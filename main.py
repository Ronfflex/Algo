from projet_part1 import *

A1 = AB()
print(A1.estVide())

A2 = AB(5)
print(A2.estVide())

A3 = AB(3)
A2.set_gauche(A3)

# ABR équilibré
Atest = AB(10, AB(5, AB(3), AB(8)), AB(12))
print(Atest.estVide())
print(Atest.taille())
print(Atest.hauteur())

print(Atest.prefixe())
print(Atest.infixe())
print(Atest.suffixe())

print(Atest.estABR())
print(Atest.estEquilibre())

print("---------------------")

# Non équilibré et non ABR
A5 = AB(10, AB(5, AB(8, AB(5)), AB(3)), AB(12))
print(A5.estVide())
print(A5.taille())
print(A5.hauteur())

print(A5.prefixe())
print(A5.infixe())
print(A5.suffixe())

print(A5.estABR())
print(A5.estEquilibre())

A5.rotationGauche()

print(A5.prefixe())

A5.rotationDroite()

print(A5.prefixe())