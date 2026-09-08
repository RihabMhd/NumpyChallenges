import numpy as np

clients=np.random.randint(18,50, size=(3, 4))
print(clients)

print(clients[0])
print(clients[:,0])
print(clients.dtype)
print(clients.shape[0])
