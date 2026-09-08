import numpy as np

notes=np.random.randint(5,20, size=(3, 5))
print(notes)

moyenne=np.mean(notes)
print(moyenne)

max_note=np.max(notes)
min_note=np.min(notes)
print("la meilleure et la plus faible note :", max_note , min_note)
print(" l'écart entre elles:",max_note-min_note)
note=notes[notes>moyenne]
print("les étudiants ayant obtenu une note supérieure à la moyenne:",note)