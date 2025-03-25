# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the total population
N = 10000

# Initial number of infected and recovered individuals
I = 1  # Initially, one person is infected
R = 0  # Initially, no one has recovered

# Everyone else is susceptible to infection initially
S = N - I - R

# Transmission rate (beta) and recovery rate (gamma)
beta = 0.3
gamma = 0.05

# Create arrays to track the evolution of S, I, and R over time
S_array = [S]
I_array = [I]
R_array = [R]

# Number of time steps
time_steps = 1000

# Loop over time steps
for t in range(time_steps):
    # Calculate probabilities
    infection_prob = beta * (I / N)  # Probability of infection
    recovery_prob = gamma           # Probability of recovery

    # Determine new infections
    new_infections = np.random.choice([0, 1], S, p=[1 - infection_prob, infection_prob]).sum()

    # Determine recoveries
    new_recoveries = np.random.choice([0, 1], I, p=[1 - recovery_prob, recovery_prob]).sum()

    # Update counts
    S = max(S - new_infections, 0)
    I = max(I + new_infections - new_recoveries, 0)
    R = min(R + new_recoveries, N)

    # Record the updated values
    S_array.append(S)
    I_array.append(I)
    R_array.append(R)

# Plot the results
plt.plot(S_array, label="Susceptible")
plt.plot(I_array, label="Infected")
plt.plot(R_array, label="Recovered")
plt.xlabel("Time Steps")
plt.ylabel("Population")
plt.title("SIR Model")
plt.legend()
plt.show()
plt . savefig ("SIR Model.png" )
