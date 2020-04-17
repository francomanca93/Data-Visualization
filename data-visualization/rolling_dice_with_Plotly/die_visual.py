from die import Die

# Create a die with 6 sides = D6
die = Die()  # instace of Die class

# Make some rolls, and store results in a list.
results = []  # A list of results
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analize the results.
frequencies = []
for value in range(1, (die.num_sides + 1)):
    frequency = results.count(value)  # .count return number of ocurrences of a value
    frequencies.append(frequency)

print(frequencies)
