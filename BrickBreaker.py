# Sai S. Bushigampala
# Resources Used: https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5

import pygame
pygame.init() #initialize pygame

win = pygame.display.set_mode((500, 500)) #set up GUI window
pygame.display.set_caption("First Python Graphics")

x = 100
y = 100
width = 70
height = 40
vel = 5
 
run = True
while run: # while GUI is running
    pygame.time.delay(50) #set a delay in ms
    
    for event in pygame.event.get(): # check for event - 
        # event - anything that Happens by User
        if event.type == pygame.QUIT: #big red close button
            run = False
            
    keys = pygame.key.get_pressed() 
    
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < 500 - height - vel:
        y +=vel
        
    rect = (x, y, width, height)
    
    win.fill((0, 0, 0)) # fill the window
    pygame.draw.rect(win, (255, 0, 0), rect)
    pygame.display.update()
    
pygame.quit() # ends the program and closes window for us
