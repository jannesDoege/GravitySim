import pygame
from simulation import Object, simulate, dt

pygame.init()

window = pygame.display.set_mode((1000, 1000))


def game_loop(objects):
    pygame.time.delay(int(dt*1000))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        window.fill(255)
        
        objects = simulate(objects)
        for o in objects:
            pygame.draw.circle(window, (255, 0, 0), (o.x+500, 500), 50)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    objects = [Object(1000, -300, 0), Object(1000, 300, 0)]
    game_loop(objects)
