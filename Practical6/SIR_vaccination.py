# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the total population
N = 10000

# Vaccination percentages to test (0%, 10%, ..., 100%)
vaccination_percentages = [i / 10 for i in range(11)]

# Store results for each vaccination percentage
results = {}

for vaccination_percentage in vaccination_percentages:
    # Initial number of vaccinated individuals
    V = int(N * vaccination_percentage)
    
    # Initial number of infected and recovered individuals
    I = 1  # Initially, one person is infected
    R = 0  # Initially, no one has recovered
    
    # Everyone else is susceptible to infection initially
    S = N - I - R - V

    # Transmission rate (beta) and recovery rate (gamma)
    beta = 0.3
    gamma = 0.05

    # Create arrays to track the evolution of S, I, and R over time
    S_array = [S]
    I_array = [I]
    R_array = [R]
    V_array = [V]

    # Number of time steps
    time_steps = 1000

    # Loop over time steps
    for t in range(time_steps):
        # Calculate probabilities
        infection_prob = beta * (I / N) if I > 0 else 0  # Probability of infection
        recovery_prob = gamma if I > 0 else 0           # Probability of recovery

        # Determine new infections
        if S > 0:
            new_infections = np.random.choice([0, 1], S, p=[1 - infection_prob, infection_prob]).sum()
        else:
            new_infections = 0

        # Determine recoveries
        if I > 0:
            new_recoveries = np.random.choice([0, 1], I, p=[1 - recovery_prob, recovery_prob]).sum()
        else:
            new_recoveries = 0

        # Update counts with boundary checks
        new_infections = min(new_infections, S)  # Ensure new infections do not exceed susceptible population
        new_recoveries = min(new_recoveries, I)  # Ensure new recoveries do not exceed infected population

        S = max(S - new_infections, 0)
        I = max(I + new_infections - new_recoveries, 0)
        R = min(R + new_recoveries, N - V)

        # Record the updated values
        S_array.append(S)
        I_array.append(I)
        R_array.append(R)
        V_array.append(V)

    # Store the results for this vaccination percentage
    results[vaccination_percentage] = I_array

# Plot the results
plt.figure(figsize=(10, 6))
for vaccination_percentage, I_array in results.items():
    plt.plot(I_array, label=f"{int(vaccination_percentage * 100)}%")

plt.xlabel("Time Steps")
plt.ylabel("Number of Infected Individuals")
plt.title("SIR Model with Different Vaccination Rates")
plt.legend(title="Vaccination Rate")
plt.grid(True)
plt.show()
plt.savefig("SIR_Model_with_Vaccination.png")