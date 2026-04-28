# Pie charts using Matplotlib in Python 

import matplotlib.pyplot as plt

labels = ("Python", "Ruby", "Rust", "Java")
sizes = [45, 65, 20, 15]

plt.pie(sizes, labels = labels, autopct = '%1.f%%', counterclock = False, startangle = 0) 

# Display the figure 
plt.show()