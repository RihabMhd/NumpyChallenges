import numpy as np

tableau = np.array([[np.nan, 15, 89, 60, np.nan],
                    [np.nan, 15, 89, 60, np.nan]])
nanvalue = np.isnan(tableau)
rows,columns=np.where(nanvalue)
positions=list(zip(rows,columns))
print(positions)
print(len(positions))
moy_general=np.nanmean(tableau)
tableau_clean=tableau.copy()
tableau_clean[nanvalue]=moy_general
print(tableau_clean)