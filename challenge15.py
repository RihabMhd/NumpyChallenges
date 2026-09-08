import numpy as np

notes = np.array([
    [14, 8, 12],
    [18, 15, 17],
    [9, 11, 10],
    [15, 13, 16]
])

print(notes.shape)

moyenne_par_matiere= np.mean(notes, axis=0)
moyenne_par_etudiant= np.mean(notes, axis=1)

print(np.min(notes))
print(np.max(notes))

moyenne_generale= np.mean(notes)
etudiants_reussi= np.where(moyenne_par_etudiant >= 10)[0]

notes_anormales= notes[notes < 10]
print(notes_anormales)