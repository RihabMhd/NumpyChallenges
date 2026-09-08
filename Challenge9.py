import numpy as np

ventes=np.random.randint(100,500,size=[12,3])
ventes_total_columns=np.sum(ventes,axis=0)
moyenne_produit=np.mean(ventes,axis=0)
print(ventes_total_columns)
print(moyenne_produit)

ventes_total_mois=np.sum(ventes,axis=1)
moyenne_mois=np.mean(ventes,axis=1)
print(ventes_total_mois)
print(moyenne_mois)

meilleur_produit=np.argmax(ventes,axis=0)
meilleur_mois=np.argmax(ventes,axis=1)

print(meilleur_mois)
print(meilleur_produit)