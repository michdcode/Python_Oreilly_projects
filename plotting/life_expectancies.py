from matplotlib import pyplot

data = open("life_expectancies_usa.txt", 'r').readlines()

dates = []
males = []
females = []

for line in data:
    date, m, f = line.split(",")
    dates.append(date)
    males.append(m)
    females.append(f)

pyplot.plot(dates, males, "bo-", label="Men")
pyplot.plot(dates, females, "mo-", label="Women")

pyplot.legend(loc="upper left")
pyplot.ylabel("Age")
pyplot.xlabel("Time")
pyplot.title("Life Expectancies over time")

pyplot.show() 