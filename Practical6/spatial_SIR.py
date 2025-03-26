# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Parameters
grid_size = 100  # Size of the grid (100x100)
beta = 0.3       # Infection probability
gamma = 0.05     # Recovery probability
time_steps = 101 # Number of time steps

# Initialize population grid
population = np.zeros((grid_size, grid_size))  # 0: Susceptible, 1: Infected, 2: Recovered

# Randomly select the initial outbreak location
outbreak = np.random.choice(range(grid_size), 2)  # Random x and y coordinates
population[outbreak[0], outbreak[1]] = 1  # Set the selected location to infected (1)

# Function to get neighbors of a cell
def get_neighbors(x, y, grid_size):
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < grid_size and 0 <= ny < grid_size:  # Ensure neighbors are within bounds
            neighbors.append((nx, ny))
    return neighbors

# Simulation loop
for t in range(time_steps):
    # Find all infected points
    infected_points = np.argwhere(population == 1)  # Get coordinates of all infected individuals

    # Create a copy of the population to update states
    new_population = population.copy()

    # Process each infected point
    for x, y in infected_points:
        # Infect susceptible neighbors
        for nx, ny in get_neighbors(x, y, grid_size):
            if population[nx, ny] == 0:  # If neighbor is susceptible
                if np.random.rand() < beta:  # Infect with probability beta
                    new_population[nx, ny] = 1

        # Recover the infected individual with probability gamma
        if np.random.rand() < gamma:
            new_population[x, y] = 2  # Recovered

    # Update the population
    population = new_population

    # Plot the population at specific time steps
    if t in [0, 10, 50, 100]:  # Plot at time steps 0, 10, 50, and 100
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.colorbar(label="State (0: Susceptible, 1: Infected, 2: Recovered)")
        plt.title(f"Population at Time Step {t}")
        plt.show()