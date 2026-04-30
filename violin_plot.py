import seaborn as sn 
import matplotlib.pyplot as plt 

data = sn.load_dataset('tips')

plt.figure(figsize=(10, 4))

sn.violinplot(x=data['total_bill'])

plt.show()