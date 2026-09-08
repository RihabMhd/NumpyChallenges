import numpy as np

temperatures=np.random.randint(14,45,size=10)

moyenne=np.mean(temperatures)

jours_chauds=temperatures[temperatures>25]
jours_froids=temperatures[temperatures<25]
temp_sup_moyenne=temperatures[temperatures>moyenne]
amplitude_thermique=np.max(temperatures)- np.min(temperatures)

print(amplitude_thermique)
print(temperatures)
print(moyenne)
print(jours_chauds)
print(jours_froids)
print(temp_sup_moyenne)
print(amplitude_thermique)