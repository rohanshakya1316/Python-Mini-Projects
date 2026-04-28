import matplotlib.pyplot as plt 

# Set up the data
labels = ("Python", "Ruby", "PHP", "Java", "Rust")

# Provides locations on x axis
index = (1, 2, 3, 4, 5)
sizes = [45, 10, 15, 30, 22]

# Set up the bar chart
plt.bar(index, sizes, tick_label = labels)

# Configure the layout 
plt.ylabel("Usuage")
plt.xlabel("Programming Languages")

# Display the chart
plt.show()