import numpy as np

scores= np.array([450, 120, 890, 340, 890, 560, 120, 990, 710])

croissant= np.sort(scores)
decroissant= np.sort(scores)[::-1]


indices_tries= np.argsort(scores)

trois_piring = croissant[:3]
trois_meilleurs = decroissant[:3]

valeurs_uniques = np.unique(scores)

print(croissant)
print(indices_tries)
print(trois_piring)
print(trois_meilleurs)
print(valeurs_uniques)