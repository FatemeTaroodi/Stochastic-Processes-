import numpy as np
import matplotlib.pyplot as plt



transition_matrix = np.array([
    [0.1, 0.6, 0.3], 
    [0.4, 0.4, 0.2], 
    [0.2, 0.3, 0.5] 
    ])


states = [0, 1, 2]


current_state = 0


num_steps = 20


state_path = [current_state]


for _ in range(num_steps):
    current_state = np.random.choice(states, p=transition_matrix[current_state])
    state_path.append(current_state)

plt.figure(figsize=(10, 5))
plt.plot(state_path, marker='o', linestyle='-', color='b', label='States Path')
plt.title('Markov Chain Simulation')
plt.xlabel('Steps')
plt.ylabel('States')
plt.xticks(range(num_steps + 1)) 
plt.yticks(states) 
plt.grid(alpha=0.5)
plt.legend()
plt.show()

