import numpy as np

clients = np.array([
    [1, 25, 80],
    [2, 30, 90],
    [3, 22, 70],
    [4, 28, 85]
])

clients[1][2]=85
clients[0]=[1, 55, 98]
clients[:,1]=[26, 31, 24, 29]
