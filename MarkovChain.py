import numpy as np
import matplotlib.pyplot as plt


# تعریف ماتریس انتقال احتمالات
transition_matrix = np.array([
    [0.1, 0.6, 0.3], # حالت 0
    [0.4, 0.4, 0.2], # حالت 1
    [0.2, 0.3, 0.5]  # حالت 2
    ])

# تعداد حالات
states = [0, 1, 2]

# حالت اولیه
current_state = 0

# تعداد گام‌های شبیه‌سازی
num_steps = 20

# لیست برای ذخیره مسیر حالت‌ها
state_path = [current_state]

# شبیه‌سازی زنجیره مارکوف
for _ in range(num_steps):
    current_state = np.random.choice(states, p=transition_matrix[current_state])
    state_path.append(current_state)
# رسم نمودار حالت ها
plt.figure(figsize=(10, 5))
plt.plot(state_path, marker='o', linestyle='-', color='b', label='States Path')
plt.title('Markov Chain Simulation')
plt.xlabel('Steps')
plt.ylabel('States')
plt.xticks(range(num_steps + 1)) # نمايش گام ها
plt.yticks(states) # نمايش همه حالت ها
plt.grid(alpha=0.5)
plt.legend()
plt.show()
