import numpy as np
from matplotlib import pyplot as plt
import os
import pandas as pd

N = 149
t = np.linspace(0, 50, N)

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'ROC curve 1.xlsx')

df1 = pd.read_excel(my_file, header = None)
curve1 = df1.iloc[:,0]
curve1 = np.array(curve1)
curve2 = df1.iloc[:,1]
curve2 = np.array(curve2)

# note that from now on, we don't have the exact formula of the curves, as we didn't save the random numbers
# we only have the points correspondent to the given t values

fig, ax = plt.subplots()
ax.plot(t, curve1,'b-')
ax.plot(t, curve1,'bo')
ax.plot(t, curve2,'r-')
ax.plot(t, curve2,'ro')

intersections = []
prev_dif = 0
t0, prev_c1, prev_c2 = None, None, None
for t1, c1, c2 in zip(t, curve1, curve2):
    new_dif = c2 - c1
    if np.abs(new_dif) < 1e-12: # found an exact zero, this is very unprobable
        intersections.append((t1, c1))
    elif new_dif * prev_dif < 0:  # the function changed signs between this point and the previous
        # do a linear interpolation to find the t between t0 and t1 where the curves would be equal
        # this is the intersection between the line [(t0, prev_c1), (t1, c1)] and the line [(t0, prev_c2), (t1, c2)]
        # because of the sign change, we know that there is an intersection between t0 and t1
        denom = prev_dif - new_dif
        intersections.append(((-new_dif*t0  + prev_dif*t1) / denom, (c1*prev_c2 - c2*prev_c1) / denom))
    t0, prev_c1, prev_c2, prev_dif = t1, c1, c2, new_dif
print(intersections)

ax.plot(*zip(*intersections), 'go', alpha=0.7, ms=10)
plt.show()