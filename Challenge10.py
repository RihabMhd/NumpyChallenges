import numpy as np

clients=np.random.randint(1,50,size=[4,4])
clients_agée=clients[clients>30]
print(clients_agée)

ages= clients[:, 0]
salaires= clients[:, 1]

combine= (ages > 30) & (salaires > 3500)
clients_filtres= clients[combine]
nb_clients= np.sum(combine)