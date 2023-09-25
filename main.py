import pygame
from random import randrange

RES = 600
SIZE = 25

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
score = 0
fps = 5

pygame.init()
window = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 18, bold=True)
font_end = pygame.font.SysFont('Arial', 32, bold=True)

while True:
    window.fill(pygame.Color('black'))
    #  drawing snake and apple
    [(pygame.draw.rect(window, pygame.Color('green'), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
    pygame.draw.rect(window, pygame.Color('red'), (*apple, SIZE - 2, SIZE - 2))
    #  show score
    render_score = font_score.render(f'SCORE: {score}', True, pygame.Color('orange'))
    window.blit(render_score, (5, 5))
    #  snake movement
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]
    #  eating apple
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        score += 1
        fps += 1
    #  game over
    if len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', True, pygame.Color('red'))
            window.blit(render_end, (RES // 2 - 100, RES // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    if x < 0:
        x = RES - SIZE + 25
    elif x > RES - SIZE:
        x = 0
    elif y < 0:
        y = RES - SIZE + 25
    elif y > RES - SIZE:
        y = 0

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #  control
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}
