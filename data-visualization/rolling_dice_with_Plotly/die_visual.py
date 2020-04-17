from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a die with 6 sides = D6
die_1 = Die()  # instace of Die class
die_2 = Die(10)
# Make some rolls, and store results in a list.
results = []  # A list of results
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analize the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, (max_result + 1)):
    frequency = results.count(value)  # .count return number of ocurrences of a value
    frequencies.append(frequency)

# Visualize the results in a Bar Chart (GRAFICO DE BARRA)

# Generating bar chart
x_values = list(range(2, max_result + 1))  # Plotly doesn't accept range() so I covert the range to a list
data = [Bar(x=x_values, y=frequencies)]

# Configurating layout. Especifically the title and the axises. 
x_axis_config = {'title': 'Result', 'dtick': 1}  # Dictionary of x axis
y_axis_config = {'title': 'Frecuency of Result'}  # Dictionary of y axis
my_layout = Layout(title='Results of rolling a D6 and a D10 50 000 times',
    xaxis=x_axis_config,
    yaxis=y_axis_config)

# Plotting data of de roll dice in a bar chart
offline.plot({'data': data, 'layout': my_layout})
# offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html') # <---- To save the bar chart

