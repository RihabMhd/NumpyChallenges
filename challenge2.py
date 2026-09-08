import numpy as np

jours=np.arange(10)

temperatures=np.linspace(5,12,10)

prix=np.zeros(7)

ids=np.ones(7)

prices=np.full([3,3],21)

print(jours, temperatures, prix, ids, prices)

print(jours.dtype)
print(temperatures.dtype)
print(prix.dtype)
print(ids.dtype)
print(prices.dtype)

