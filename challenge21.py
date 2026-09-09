import numpy as np

a=np.array([
    [20, 3000, 800],
    [25, 5000, 1200],
    [30, 7000, 1500]
])

print(a.shape)

b=np.array([18,8000,1300])

res=a+b

print(res)

#So NumPy says:
#"B has 3 elements, and A has 3 columns. I can apply B to each row."
#It conceptually expands B

#Vectorisation = performing an operation on an entire NumPy array at once, instead of using Python loops.