triangle_numbers = []
# Loop from 1 to 10 (since we want to calculate the first ten values)
for n in range(1, 11):
    # Initialize the sum of the current triangular number to 0
    sum = 0
    # Loop from 1 to n to calculate the sum from 1 to n
    for i in range(1, n + 1):
        sum += i
    # Add the calculated sum to the list
    triangle_numbers.append(sum)

# Iterate through the list and print each triangular number
for number in triangle_numbers:
    print(number)

