# Create a lambda which returns the first item in a list.
import math

names = ["Angel", "Mihail", "Grigor", "Stefan"]

var = lambda list: print(list[0])
var(names)


# Map a lambda which applies the logistic function to the list [-3, -5, 1, 4] .
# Round each number to 4 decimal places.

numbers = [-3, -5, 1, 4]

results = map(lambda x: round((1 / (1 + math.exp((- 1) * x))), 4), numbers)
print(list(results))
