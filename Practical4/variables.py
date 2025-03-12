# The time it takes to walk to the bus stop, in minutes
a = 15
# The time it takes to take the bus. Convert 1 hour and 15 minutes to minutes
b = 60 + 15
# Calculate the total commuting time by bus
c = a + b

# The time it takes to drive. Convert 1 hour and 30 minutes to minutes
d = 60 + 30
# The time it takes to walk from the parking lot, in minutes
e = 5
# Calculate the total commuting time by car
f = d + e

# Compare the total commuting times of the two methods
if c < f:
    print("Commuting by bus is faster. The total commuting time by bus is {} minutes, and the total commuting time by car is {} minutes.".format(c, f))
elif c > f:
    print("Commuting by car is faster. The total commuting time by bus is {} minutes, and the total commuting time by car is {} minutes.".format(c, f))
else:
    print("The commuting times of the two methods are the same. The total time is {} minutes for both.".format(c))

#Boolean
# Create Boolean variable X and initialize it to True
X = True
# Create Boolean variable Y and initialize it to False
Y = False

# Create variable W, representing the "and" relationship between X and Y
W = X and Y

# Print the value of variable W
print("The value of W is:", W)

# Truth table for W (i.e., X and Y):
# | X | Y | W（X and Y）|
# |---|---|-------------|
# | T | T | T           |
# | T | F | F           |
# | F | T | F           |
# | F | F | F           |
