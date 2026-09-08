import numpy as np

ventes= np.random.randint(100, 500, size=[12, 3])

ventes_total_produits= np.sum(ventes, axis=0)
moyenne_produits= np.mean(ventes, axis=0)

ventes_total_mois= np.sum(ventes, axis=1)
moyenne_mois= np.mean(ventes, axis=1)

meilleur_produit= np.argmax(ventes_total_produits)
meilleur_mois= np.argmax(ventes_total_mois)

print(meilleur_produit)
print(meilleur_mois)