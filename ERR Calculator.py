# Source: https://kitchingroup.cheme.cmu.edu/blog/2013/07/04/Estimating-where-two-functions-intersect-using-data/

import os
import pandas as pd
import numpy as np
from pycse import regress
import matplotlib.pyplot as plt
import uncertainties as u
from scipy.optimize import fsolve


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'ROC curve 1.xlsx')
df1 = pd.read_excel(my_file, header = None)
curve1 = df1.iloc[:,0]
curve2 = df1.iloc[:,1]
#curve1.plot()
#curve2.plot()
#plt.show()

T = np.array(np.linspace(0,1,419))
print(T)
E1 = np.array(curve1)
print("T length " + str(E1.size))
E2 = np.array(curve2)
print("T length " + str(E2.size))
E = E1 - E2

# columns of the x-values for a line: constant, T
A = np.column_stack([T**0, T])

p, pint, se = regress(A, E, alpha=0.005)

b = u.ufloat((p[0], se[0]))
m = u.ufloat((p[1], se[1]))

@u.wrap
def f(b, m):
    X, = fsolve(lambda x: b + m * x, 800)
    return X

print("EER point is " + str(f(b, m)))
