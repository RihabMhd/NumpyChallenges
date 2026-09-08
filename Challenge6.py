import numpy as np

ventes = np.random.randint(1000, 9000, size=10)


ca_brut= np.sum(ventes)
ca_apres_remise= ventes * 0.90  
ca_avec_tva= ca_apres_remise * 1.20  

nombre_ventes= ventes.size
vente_moyenne= np.mean(ventes)
min_ventes= np.min(ventes)
max_ventes= np.max(ventes)

print(ca_apres_remise)
print(ca_avec_tva)
print(vente_moyenne)