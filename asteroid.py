import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)
    
    
    def draw(self, screen) -> None:
        pygame.draw.circle(surface=screen, color='white', center=self.position, radius=self.radius, width=2)
    
    
    def update(self, dt:float) -> None:
        self.position += self.velocity * dt 