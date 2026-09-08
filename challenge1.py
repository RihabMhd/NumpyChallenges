import numpy as np

tab1=np.random.randint(5000,size=10)
print(tab1)

print("Shape:",tab1.shape)
print("Dimensions:",tab1.ndim)
print("Size:",tab1.size)
print("Type:",tab1.dtype)

print(tab1[0])
print(tab1[-1])
print(np.min(tab1))
print(np.max(tab1))
print(np.mean(tab1))