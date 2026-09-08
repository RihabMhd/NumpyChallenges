import numpy as np

notes=np.random.randint(5,20, size=(3, 5))
print(notes)

moyennes=np.mean(notes, axis=0)
max_matiere=np.max(notes, axis=0)
min_matiere=np.min(notes, axis=0)
ecart_matiere=max_matiere - min_matiere
print(moyennes)
print(ecart_matiere)

etudiants_superieurs= notes > moyennes
print(etudiants_superieurs)