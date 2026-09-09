import numpy as np

vecteur=np.arange(1,601)
#print(vecteur)

matrice=vecteur.reshape(20,30)
#print(matrice)

threeD_tab=vecteur.reshape(10,10,6)
#print(threeD_tab)

print(vecteur.shape)
print(matrice.shape)
print(threeD_tab.shape)

print(vecteur.ndim)
print(matrice.ndim)
print(threeD_tab.ndim)

print(vecteur.size)
print(matrice.size)
print(threeD_tab.size)

# flatten() → retourne une copie aplatie (1D).
# ravel() → retourne une vue aplatie si possible (plus rapide, mais modifier l original)
print(matrice.flatten())
print(matrice.ravel())



