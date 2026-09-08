import numpy as np

data = np.array([
    22.5, 23.1, -999,  21.8, np.nan, 24.0,
    150.0, 22.9, 23.5, np.nan, -5.2, 22.1,
    23.8, np.nan, 999.9, 21.5, 22.7, -50.0,
    23.0, 22.4
])

nanvalue=np.isnan(data)
rows = np.where(nanvalue)[0]
positions = list(zip(rows))
print(positions)

negvalue = data < 0
rowsN = np.where(negvalue)[0]
positionsN = list(zip(rowsN))
print(positionsN)

mean=np.nanmean(data)
std=np.nanstd(data)
scores=(data-mean)/std
number=data[np.abs(scores)>2]
print(number)

badvalues=nanvalue | negvalue
clean = data[~badvalues]
print(clean)