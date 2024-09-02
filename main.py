from doctest import FAIL_FAST
import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def create_group() -> pygame.sprite.Group:
    return pygame.sprite.Group()


def main():
    print("Starting")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.flip()
    
    clock = pygame.time.Clock()

    asteroids = create_group()
    updatable = create_group()
    drawable = create_group()
    shotable = create_group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shotable, updatable, drawable)
    
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    dt = 0
    
    is_running: bool = True
    
    while is_running:
        print("Running")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        
        for object in updatable:
            object.update(dt=dt)
        
        for asteroid in asteroids:
            if asteroid.collided_with(player):
                print("Game over!")
                sys.exit(0)
            
            for shot in shotable:
                if asteroid.collided_with(shot):
                    shot.kill()
                    asteroid.split()
                    
        
        screen.fill('black')
        
        for object in drawable:
            object.draw(screen=screen)

        
        dt = clock.tick(60) / 1000
        print("FPS: ", dt)
        
    
main()