import numpy as np


clients = np.array([
    [20, 1500, 3],
    [35, 2000, 8],
    [26, 3400, 2]
])

client=np.array([36,2800,6])

distance_euclidien=np.linalg.norm(clients-client,axis=1)
print(distance_euclidien)

le_plus_proche=np.argmin(distance_euclidien)
le_plus_loins=np.argmax(distance_euclidien)

print(le_plus_proche,le_plus_loins)