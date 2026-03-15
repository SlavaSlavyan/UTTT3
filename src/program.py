# main class of the program, as well as its center

import pygame
import sys

from src.display import Display
from src.event import Event
from util.sceneLoader import Scene

class Program:

    def __init__(self, version:str):

        self.version = version

        pygame.init()

        self.status = "Game"

        self.Display = Display(self)
        self.Event = Event(self)
        self.Scene = Scene(self)

        self.Display.on_resize(self)

    def main(self): # main function of the program

        while (True):

            self.Event.main(self)

            self.Display.main(self)

            pygame.display.flip()

            self.Display.Clock.tick(60)

    def stop(self):

        pygame.quit()
        sys.exit()