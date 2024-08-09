import numpy as np
import json
import GameSimulator as gs
import time
import pygame

# Retrieve the list from the JSON file
with open('q_table.json', 'r') as json_file:
    loaded_list = json.load(json_file)

loaded_array = np.array(loaded_list)

done = False
target = [9, 9]
input_loop = True

while input_loop:
    print("Enter the state coordinates x ,y -  separated by a comma: ", end="")
    state = input()
    if state == "exit":
        exit()
    else:
        try:
            x, y = map(lambda x: int(x.strip()), state.split(","))
            print("Q-values for state ({}, {}): {}".format(x,
                                                           y, loaded_array[x, y]))
            simulator = gs.GameSimulator(500, 10, [x, y], target)
            simulator.draw_game()
            time.sleep(2)
            input_loop = False
        except:
            print("Invalid input. Please enter two integers separated by a comma.")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    next_state = np.argmax(loaded_array[x, y])

    if next_state == 3:
        simulator.go_up()
    elif next_state == 2:
        simulator.go_right()
    elif next_state == 1:
        simulator.go_down()
    elif next_state == 0:
        simulator.go_left()

    x, y = simulator.animal_position
    print("Current state: ({}, {})".format(x, y))

    if x == simulator.target_position[0] and y == simulator.target_position[1]:
        print("Congratulations! You have reached the target state.")
        done = True

    simulator.draw_game()
    time.sleep(1)

simulator.quit_game()
