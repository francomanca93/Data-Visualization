# %%
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk
rw = RandomWalk()  # We create a object from the RandomWalk class
rw.fill_walk()  # We call the method fill_walk()

# Plot the points in the walk.
plt.style.use('seaborn')
fig = plt.subplot() 
ax = plt.subplot()  
ax.scatter(rw.x_values, rw.y_values, s=10)

# Set chart tittle and label axes.
ax.set_title("Random Walks", fontsize=20)
ax.set_xlabel("X values", fontsize=14)
ax.set_ylabel("Y values", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=10)

plt.show()




# %%
