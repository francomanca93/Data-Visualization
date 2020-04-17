from random import choice  # 

class RandomWalk:
    """ A class to generate random walks.
        Una clase para generar caminos aleatorios.
    """

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points  # Variable to store the nomber of points in the walk

        # All walks start at (0, 0). Two list to store coordinate of each point in the walk
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        """Calculate all the points in the walk."""
    
        # Keep taking steps until the walk reaches the desired lenght.
        while len(self.x_values) < self.num_points:
            
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        """Determinate the direction and distance for each step"""
        
        # This method tells Python how to simulate four random decisions
        # 1: Will the walk go right or left?
        # 2: How far will ir go in that direction?
        # 3: Will it go up or down?
        # 4: How far will it go in that direction?

        # Decide wich direction to go and how far to go in that direction.
        coordinate_direction = choice([1, -1])  # 1 = Right direction, -1 = Left direction
        coordinate_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8]) # distance traveled 
        coordinate_step = coordinate_direction * coordinate_distance # Go...
        return coordinate_step




