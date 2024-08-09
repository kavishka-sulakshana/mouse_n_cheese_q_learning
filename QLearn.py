import random
import numpy as np
import pygame
import GameSimulator as gs
import matplotlib.pyplot as plt
import seaborn as sns
import time
import json

# Define the environment parameters
grid_size = (10, 10)
start = (0, 0)
target = (9, 9)
obstacles = []
window_size = 500

simulator = gs.GameSimulator(
    window_size, grid_size[0], list(start), list(target))

# Initialize Q-table
q_table = np.zeros((grid_size[0], grid_size[1], 4))  # 4 actions

# Hyperparameters
alpha = 0.1  # Learning rate
gamma = 0.99  # Discount factor
epsilon = 1.0  # Initial exploration rate
epsilon_decay = 0.995
epsilon_min = 0.01
num_episodes = 500


def do_action(action):
    # Actions: 0=left, 1=down, 2=right, 3=up
    if action == 3:
        simulator.go_up()
    elif action == 2:
        simulator.go_right()
    elif action == 1:
        simulator.go_down()
    elif action == 0:
        simulator.go_left()

    if simulator.animal_position[0] == target[0] and simulator.animal_position[1] == target[1]:
        return target, 1, True
    else:
        return tuple(simulator.animal_position), -0.01, False


def plot_q_table(q_table):
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(np.max(q_table, axis=2), annot=True, cmap='YlGnBu', ax=ax)
    ax.set_title('Maximum Q-value for each state')
    plt.show()


def plot_policy(q_table):
    policy = np.argmax(q_table, axis=2)
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(np.zeros(grid_size), cbar=False,
                annot=policy, fmt='d', cmap='coolwarm', ax=ax)
    ax.set_title('Optimal policy (0=up, 1=right, 2=down, 3=left)')
    plt.show()


# Q-learning algorithm
state = tuple(simulator.reset_game())
for episode in range(num_episodes):
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action = random.choice(range(4))
        else:
            # Exploit learned values
            action = np.argmax(q_table[state[0], state[1]])

        # Take action, observe new state and reward
        next_state, reward, done = do_action(action)

        # Update Q-table
        best_next_action = np.argmax(q_table[next_state[0], next_state[1]])
        q_table[state[0], state[1], action] += alpha * (
            reward + gamma * q_table[next_state[0], next_state[1], best_next_action] -
            q_table[state[0], state[1], action]
        )

        # Move to the next state
        state = next_state
        simulator.draw_game()
        time.sleep(0.001)

    # Decay epsilon
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay
    state = (0, 0)
    simulator.reset_game()
    simulator.draw_game()
    print("Episode:", episode, "Epsilon:", epsilon, "state:", state)
    time.sleep(0.05)

with open('example3/q_table.json', 'w') as json_file:
    json.dump(q_table.tolist(), json_file)

print("Q-table saved to q_table.json")

# plot the Q-table values
plot_q_table(q_table)
plot_policy(q_table)  # plot the directions

simulator.quit_game()
