from const import *
import pygame


pygame.init()
window = pygame.display.set_mode((SIZE_WINDOW_X, SIZE_WINDOW_Y))
pygame.display.set_caption('Connect 4')

images = dict()
images['background.png'] = pygame.image.load('img/background.png')
images['red_piece.png'] = pygame.image.load('img/red_piece.png')
images['yellow_piece.png'] = pygame.image.load('img/yellow_piece.png')

window.blit(images['background.png'], (0,0))
pygame.display.flip()


input()