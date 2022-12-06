import vector
import pygame

from vector import Vector

delta_time = 0.001
screen = pygame.display.set_mode((960, 720))


class Ball:
    def __init__(self, position: Vector, velocity_tangential: Vector = Vector(0, 0), velocity_angular: Vector = Vector(0, 0), radius: float = 8, color=(255,255,255)):
        self.position = vector.copy(position)
        self.velocityT = vector.copy(velocity_tangential)
        self.velocityA = vector.copy(velocity_angular)
        self.radius = radius
        self.diameter = radius * 2.0
        self.color = color
        self.resultant_vel = self.velocityT + self.velocityA

        self.alive = True

    def update(self):
        self.velocityT += delta_time * 2  # 2 is arbitrary tangential acceleration
        self.velocityA += delta_time * 2  # 2 is arbitrary angular acceleration
        self.resultant_vel.x += self.velocityT.x + self.velocityA.x
        self.resultant_vel.y += self.velocityT.y + self.velocityA.y
        self.position += self.resultant_vel * delta_time
        self.check_screen_collisions()

    def draw(self):
        top_left_position = self.position - self.radius
        pygame.draw.circle(screen, self.color, top_left_position.make_int_tuple(), 10)

    def check_screen_collisions(self):
        if self.position.x < self.radius or self.position.x > 960 - self.radius:
            self.resultant_vel = -self.resultant_vel

        if self.position.y < self.radius or self.position.y > 720 + self.radius:
            self.resultant_vel = -self.resultant_vel
