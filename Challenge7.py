import numpy as np

salaire_employee= np.random.randint(3500, 8000, size=20)

moyenne= np.mean(salaire_employee)
median= np.median(salaire_employee)
variance= np.var(salaire_employee)  
ecart_type= np.std(salaire_employee)
min_salaire= np.min(salaire_employee)
max_salaire= np.max(salaire_employee)

#le percentile indique la valeur sous laquelle se trouve un pourcentage précis de tes données
q1= np.percentile(salaire_employee, 25)
q3= np.percentile(salaire_employee, 75)  

print(f"Variance: {variance}, Q1: {q1}, Q3: {q3}")