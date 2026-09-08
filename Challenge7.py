import numpy as np

salaire_employee=np.random.randint(3500,8000,size=20)

moyenene=np.mean(salaire_employee)

median=np.median(salaire_employee)

ecart_type=np.std(salaire_employee)

min_salaire=np.min(salaire_employee)

max_salaire=np.max(salaire_employee)

q1=np.percentile(salaire_employee,25)

q2=np.percentile(salaire_employee,75)

print(q1)