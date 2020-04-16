# %%
# Los dos %% me permiten utilizar python interactive en VSCode 
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fix, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds , s=10)  # This method allow me ploting a single point

# Set chart tittle and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')
# With the up line you can save the plot to a file. 

# %%
