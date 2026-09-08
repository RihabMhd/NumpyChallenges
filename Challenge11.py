import numpy as np 

tableau=np.array([12, 48, 49, 16, 72, 36, 26, 46])

seuil_max=50
seuil_min=20

mes_normal=(tableau>seuil_min) & (tableau<seuil_max)
mes_sus=(tableau<seuil_min) | (tableau>seuil_max)

valeurNormal=tableau[mes_normal]
valeurSus=tableau[mes_sus]
nombreSus=np.size(valeurSus)
positionsSus=np.where(valeurSus)

print(valeurNormal)
print(valeurSus)
print(nombreSus)
print(positionsSus)