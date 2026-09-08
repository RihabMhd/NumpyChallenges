import numpy as np

ventes=np.random.randint(1000,9000,size=10)
print(ventes)
ca=np.sum(ventes)/np.size(ventes)
print(ca)

nombre_ventes=np.size(ventes)
max_ventes=np.max(ventes)
min_ventes=np.min(ventes)

vente_moyenne=np.mean(ventes)
print(vente_moyenne)