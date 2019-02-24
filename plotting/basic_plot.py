from matplotlib import pyplot
import random

random.randint(0, 30)

x_values = [0, 2, 4, 8, 16, 32]
y_values = [random.randint(0, 30) for element in x_values]

pyplot.plot(x_values, y_values, "o-")

pyplot.ylabel("Value")
pyplot.xlabel("Time")
pyplot.title("Test plot")

pyplot.show()
