# %% 
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig = plt.subplot()
ax = plt.subplot()  # subplot() --> this function can be generate plots in the same figure

ax.plot(input_values, squares, linewidth=2)
ax.plot()

# Set chart tittle and label axes.
ax.set_title("Square Numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()  # The function show() opens matplotlib's viewer and display the plot.


# %%
