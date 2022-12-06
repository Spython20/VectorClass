import pygame

import vector
from vector import *
import entities
from ball import Ball

pygame.display.set_caption('Power Pool')


def update():
    entities.update_balls()


def draw():
    screen.fill((50, 50, 50))
    entities.draw_balls()


pygame.init()

screen = pygame.display.set_mode((960, 720))

app_running = True
clock = pygame.time.Clock()

# creates ball
entities.balls.append(
    Ball(Vector(300, 300), vector.random_vector() * 25, vector.random_vector() * 25))

while app_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                app_running = False

    # game loop functions
    update()
    draw()
    print(entities.balls[0].position.y, entities.balls[0].resultant_vel.y, entities.balls[0].velocityA.y, entities.balls[0].velocityT.y)

    pygame.display.flip()
    delta_time = 0.001 * clock.tick(144)

pygame.quit()
