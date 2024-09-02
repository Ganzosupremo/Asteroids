import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player

def create_group() -> pygame.sprite.Group:
    return pygame.sprite.Group()


def main():
    print("Starting")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = create_group()
    updatable = create_group()
    drawable = create_group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    dt = 0
    
    while True:
        print("Running")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for object in updatable:
            object.update(dt=dt)
        
        screen.fill('black')
        
        for object in drawable:
            object.draw(screen=screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        print("FPS: ", dt)
        
    
main()