import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_simulations = int(input("Enter the number of simulations: "))
max_generations = int(input("Enter the maximum number of generations: "))
p = float(input("Enter the probability of having 0 offspring: "))
q = float(input("Enter the probability of having 1 offspring: "))
r = 1 - p - q  # Probability of having 2 offspring

# Validate probabilities
if r < 0 or not np.isclose(p + q + r, 1):
    raise ValueError("The probabilities must sum to 1 and must not be negative.")

initial_population = int(input("Enter the initial population size: "))
if initial_population <= 0:
    raise ValueError("Initial population size must be greater than 0.")

# Store extinction generations
extinction_generations = []

for sim in range(num_simulations):
    population = initial_population
    
    for generation in range(max_generations):
        new_population = 0

        # Generate offspring for the current population
        for _ in range(population):
            offspring = np.random.rand()
            if offspring < p:
                new_population += 0
            elif offspring < p + q:
                new_population += 1
            else:
                new_population += 2

        population = new_population

        # Check extinction
        if population == 0:
            extinction_generations.append(generation + 1)
            break
    else:
        # If no extinction, append max_generations
        extinction_generations.append(max_generations)

# Calculate extinction probability
extinction_probability = sum(gen < max_generations for gen in extinction_generations) / num_simulations

# Display results
print(f"Extinction probability: {extinction_probability:.4f}")

# Plot the histogram of extinction generations
plt.hist(extinction_generations, bins=range(1, max_generations + 2), edgecolor="k", alpha=0.7)
plt.title("Distribution of Generations Until Extinction")
plt.xlabel("Generations Until Extinction")
plt.ylabel("Number of Simulations")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
