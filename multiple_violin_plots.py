import seaborn as sn

import matplotlib.pyplot as plt 

data = sn.load_dataset('tips')
plt.figure(figsize= (6, 4)) 
sn.violinplot(x='day', y='total_bill', data=data)
plt.show()