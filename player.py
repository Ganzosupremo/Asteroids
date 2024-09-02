import circleshape
import pygame
from constants import *
from shot import Shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)
        
        self.shot_cooldown: float = 0.0
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def shoot(self) -> None:
        if self.shot_cooldown > 0.0:
            return

        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN
        
    def draw(self, screen) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def move(self, dt: float) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def rotate(self, dt: float) -> None:
       self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.shot_cooldown -= dt
        
        if keys[pygame.K_a]:
            self.rotate(dt=-dt)
        if keys[pygame.K_d]:
            self.rotate(dt=dt)
        if keys[pygame.K_w]:
            self.move(dt=dt)
        if keys[pygame.K_s]:
            self.move(dt=-dt)
            
        if keys[pygame.K_SPACE]:
            self.shoot()
        
    
    