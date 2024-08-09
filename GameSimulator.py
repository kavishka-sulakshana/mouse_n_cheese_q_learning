import pygame
import sys


class GameSimulator:
    def __init__(self, window_size=500, grid_size=5, start_position=[0, 0], target_position=[4, 4], animal_image="example3/images/mouse.png", cheese_image="example3/images/cheese.png", caption="Grid with Animal") -> None:
        self.window_size = window_size
        self.grid_size = grid_size
        self.cell_size = window_size // grid_size
        self.destination_color = (255, 0, 0)
        self.start_position = start_position
        self.animal_position = self.start_position
        self.destination = None
        self.running = True
        self.target_position = target_position
        self.screen = pygame.display.set_mode((window_size, window_size))
        self.animal_image = pygame.image.load(animal_image)
        self.food_image = pygame.image.load(cheese_image)
        self.animal_image = pygame.transform.scale(
            self.animal_image, (self.cell_size, self.cell_size))
        self.food_image = pygame.transform.scale(
            self.food_image, (self.cell_size, self.cell_size))
        pygame.init()
        pygame.display.set_caption(caption)

    def draw_grid(self):
        for x in range(0, self.window_size, self.cell_size):
            for y in range(0, self.window_size, self.cell_size):
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)

    def validate_move(self, position, direction):
        if direction == "UP":
            position = [position[0], position[1] - 1]
        elif direction == "DOWN":
            position = [position[0], position[1] + 1]
        elif direction == "LEFT":
            position = [position[0] - 1, position[1]]
        elif direction == "RIGHT":
            position = [position[0] + 1, position[1]]
        return False if position[0] < 0 or position[0] >= self.grid_size or position[1] < 0 or position[1] >= self.grid_size else True

    def go_up(self):
        if self.validate_move(self.animal_position, "UP"):
            self.animal_position[1] -= 1
        return self.animal_position

    def go_down(self):
        if self.validate_move(self.animal_position, "DOWN"):
            self.animal_position[1] += 1
        return self.animal_position

    def go_left(self):
        if self.validate_move(self.animal_position, "LEFT"):
            self.animal_position[0] -= 1
        return self.animal_position

    def go_right(self):
        if self.validate_move(self.animal_position, "RIGHT"):
            self.animal_position[0] += 1
        return self.animal_position

    def draw_game(self):
        self.screen.fill((255, 255, 255))
        self.draw_grid()
        animal_rect = pygame.Rect(
            self.animal_position[0] * self.cell_size, self.animal_position[1] * self.cell_size, self.cell_size, self.cell_size)
        food_rect = pygame.Rect(
            self.target_position[0] * self.cell_size, self.target_position[1] * self.cell_size, self.cell_size, self.cell_size)
        self.screen.blit(self.food_image, food_rect)
        self.screen.blit(self.animal_image, animal_rect)
        pygame.display.flip()

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def reset_game(self):
        self.animal_position = [0, 0]
        self.destination = None
        return self.animal_position
