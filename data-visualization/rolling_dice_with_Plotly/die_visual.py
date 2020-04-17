from die import Die

# Create a die with 6 sides = D6
die = Die()  # instace of Die class

# Make some rolls, and store results in a list.
results = []  # A list of results
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)
