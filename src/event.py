# pygame event handler

import pygame

from util.mouseInput import Mouse

class Event:

    def __init__(self, mainself):
        
        self.Mouse = Mouse(mainself)

    def main(self, mainself):
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                mainself.stop()

            if event.type == pygame.VIDEORESIZE:
                mainself.Display.on_resize(mainself)
            
            self.Mouse.main(mainself, event)
        
        self.Mouse.update(mainself)