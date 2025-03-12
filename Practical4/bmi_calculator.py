# Prompt the user to enter their weight in kilograms and store the input as the variable 'weight'
weight = float(input("Please enter your weight in kg: "))
# Prompt the user to enter their height in meters and store the input as the variable 'height'
height = float(input("Please enter your height in m: "))

# Calculate the BMI using the formula BMI = weight (kg) / (height (m) ** 2)
BMI = weight / (height ** 2)

# Determine the weight status based on the value of BMI
if BMI < 18.5:
    status = "underweight"
elif BMI <= 30:
    status = "normal weight"
else:
    status = "obese"

# Construct the output message, including the value of BMI and the weight status
output = "Your BMI is " + str(BMI) + ". You are considered " + status + "."

# Print the output message
print(output)