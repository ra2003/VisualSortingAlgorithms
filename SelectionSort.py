import pygame
import sys
from random import shuffle
from math import sqrt, ceil
from time import sleep
from threading import Thread

pygame.init()
(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
unsorted = [i for i in range(1, 250)]
shuffle(unsorted)
n = len(unsorted)
QUIT_SIGNAL = False
offset = 0
if n <= 100:
    offset = ceil(sqrt(100 - n))
delay = 5 / 1000  # Milli


def main():
    for i in range(n):
        pygame.draw.rect(screen, WHITE,
                         (i * (width / n), height - (unsorted[i] * (height / n)), (width / n) - offset, height))
    pygame.display.update()

    while not QUIT_SIGNAL:
        if sorted(unsorted) != unsorted:
            SelectionSort(unsorted)


def SelectionSort(unsorted):
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if unsorted[min_idx] > unsorted[j]:
                min_idx = j
        unsorted[i], unsorted[min_idx] = unsorted[min_idx], unsorted[i]
        sleep(delay)
        UpdateDisplay(min_idx)
        UpdateDisplay(i, (0, 255, 0))
        if QUIT_SIGNAL:
            return

    [UpdateDisplay(i, (0, 255, 0)) for i in range(n)]


def CheckInput():
    global QUIT_SIGNAL
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QUIT_SIGNAL = True
                return
        sleep(1)


def UpdateDisplay(i, color=(255, 255, 255)):
    pygame.draw.rect(screen, BLACK, (i * (width / n), 0, (width / n) - offset, height))
    pygame.draw.rect(screen, color,
                     (i * (width / n), height - (unsorted[i] * (height / n)), (width / n) - offset, height))
    pygame.display.update()


if __name__ == '__main__':
    Thread(target=CheckInput, ).start()
    main()
    pygame.quit()
    sys.exit(0)
