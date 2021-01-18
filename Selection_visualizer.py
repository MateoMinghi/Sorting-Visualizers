import pygame as pg
import sys
import random

#colors for the visualizer
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (255, 0, 255)

#window parameters
WIDTH = 680
HEIGHT = 500
window_size = (WIDTH, HEIGHT)

#initialize pygame
pg.init()

#more window parameters
win = pg.display.set_mode(window)
pg.display.set_caption('Selection Sort')
clock = pg.time.Clock()

n = 4
division = abs(int(WIDTH/n))

#array that is going to be sorted
h_arr = []
#state (sorted, unsorted)
state = []

for i in range(division):
  #creating randomly-sized bars
  bar_height = random.randint(0, HEIGHT)
  #the array is now going to be filled
  h_arr.append(bar_height)
  state.append(1)
  
 counter = 0
 
 def Algorithm(h_arr, state, counter):
  while Algorithm:
    win.fill((0, 0, 0))
    
    if counter < len(h_arr):
      min_value = counter
      
      for j in range(counter+1, len(h_arr)):
        #if any element is smalled than the smallest value, then that element is the real smallest value
        if h_arr[j] < h_arr[min_value]:
          min_value = j
          state[j] = 0
         else:
          state[j] = 1
          state[min_value] = 1
         #swapping elements is the array
         h_arr[counter], h_arr[min_value] = h_arr[min_value], h_arr[counter]
     counter+1
      
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
                #creating the rectangles graphically
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
    algorithm(h_arr, state, counter)
         
