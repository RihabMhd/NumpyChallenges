import numpy as np

clients=np.random.randint(1,50,size=[4,4])
clients_agée=clients[clients>30]
print(clients_agée)