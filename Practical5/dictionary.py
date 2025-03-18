# Create a dictionary to record the programming languages and their corresponding 
# percentages of developers using them.
language_percentage = {
    "JavaScript": 62.3,
    "HTML": 52.9,
    "Python": 51,
    "SQL": 51,
    "TypeScript": 38.5
}
# Print the dictionary.
print(language_percentage)

# Import the pyplot module from the matplotlib library for plotting.
# Make sure you have installed the matplotlib library (you can use "pip install matplotlib" to install it).
import matplotlib.pyplot as plt

# Extract the programming languages (keys) from the dictionary into a list.
languages = list(language_percentage.keys())
# Extract the percentages (values) from the dictionary into a list.
percentages = list(language_percentage.values())

# Create a bar plot.
plt.bar(languages, percentages)
# Set the label for the x - axis.
plt.xlabel('Programming Languages')
# Set the label for the y - axis.
plt.ylabel('Percentage of Users')
# Set the title for the plot.
plt.title('Popularity of Programming Languages in February 2024')
# Display the plot.
plt.show()

# Assume we want to check the percentage of developers using SQL.
# Instead of taking user input, we create a variable that can be modified.
requested_language = "SQL"
# Check if the requested language exists in the dictionary.
if requested_language in language_percentage:
    print(f"The percentage of developers who use {requested_language} is {language_percentage[requested_language]}%")
else:
    print(f"{requested_language} not found in the data.")