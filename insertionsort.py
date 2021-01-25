import pygame as pg
import random
import sys

RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

WIDTH = 600
HEIGHT = 500
window_size = (WIDTH, HEIGHT)

pg.init()

win = pg.display.set_mode(window_size)
pg.display.set_caption('Insertion Sort')
clock = pg.time.Clock()

n = 4
division = int(WIDTH/n)

h_arr = []
state = []

def filling_array(h_arr, state): 
    for i in range(division):
        height = random.randint(0, HEIGHT)
        h_arr.append(height)
        state.append(1)

counter = 0

def InsertionSort(h_arr, state, counter):
    filling_array(h_arr, state)
    while InsertionSort:
        win.fill((0, 0, 0))

        if counter < len(h_arr):

            key = h_arr[counter]
            j = counter - 1 

            while j >= 0 and h_arr[j] > key:
                h_arr[j], h_arr[j+1] = h_arr[j-1], h_arr[j]
                j -= 1
            h_arr[j+1] = key
        counter += 1


        if counter - 1 < len(h_arr):
            state[counter - 1] = 2

        #changing the colors of the rectangles depending on their state
        for i in range(len(h_arr)):
            if state[i] == 0:
                color = RED
            elif state[i] == 2:
                color = GREEN  
            else:
                color = WHITE
            pg.draw.rect(win, color, pg.Rect(int(i*n), HEIGHT - h_arr[i], n, h_arr[i]))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        #speed of the sorting
        clock.tick(30)
        pg.display.flip()

    return h_arr

if __name__ == "__main__":
    InsertionSort(h_arr, state, counter)