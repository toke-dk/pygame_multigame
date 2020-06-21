import pygame
from player import Player
from network import Network

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Client')


def redraw_window(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    # tager det fra player object og ser hvilken player det er lige nu
    p = n.get_p()
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redraw_window(win, p, p2)


main()
