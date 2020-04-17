# %%
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active
while True: # <------- Comment this line and others that it have arrows if you'll run in jupyter
    # Make a random walk
    rw = RandomWalk(50_000)  # We create a object from the RandomWalk class
    rw.fill_walk()  # We call the method fill_walk()

    # Plot the points in the walk.
    plt.style.use('seaborn')
    fig = plt.subplot() 
    ax = plt.subplot()  
    
    # Plotting the cloud points
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, 
        c=point_numbers, 
        cmap=plt.cm.Blues,
        edgecolors='none', 
        s=1)

    # Emphasize the first and last points.
    ax.scatter(0, 0, 
        c='green',
        edgecolors='none',
        s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1],
        c='red',
        edgecolors='none', 
        s=100)

    # Set chart tittle and label axes.
    ax.set_title("Random Walks", fontsize=20)
    ax.set_xlabel("X values", fontsize=14)
    ax.set_ylabel("Y values", fontsize=14)

    # Set size of tick labels.
    ax.tick_params(axis='both', which='major', labelsize=10)

    # Remove the axes.
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")  # <------- Comment this line if you'll run in jupyter
    if keep_running == 'n':  # <------- Comment this line if you'll run in jupyter
        break  # <------- Comment this line if you'll run in jupyter

