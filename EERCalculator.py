import pandas as pd
import matplotlib.pyplot as plt
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'ROC curve 1.xlsx')

excel1 = pd.ExcelFile(my_file)
#excel1.sheet_names
df1 = excel1.parse()
df1.plot()
plt.show()
#print(df1)