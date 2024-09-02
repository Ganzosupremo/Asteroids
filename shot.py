import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen) -> None:
        pygame.draw.circle(surface=screen, color='white', center=self.position, radius=self.radius, width=2)
    
    
    def update(self, dt:float) -> None:
        self.position += self.velocity * dt 