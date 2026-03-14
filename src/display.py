# class responsible for all visualization in the program

import pygame

class Display:

    def __init__(self, mainself):

        self.colors = {
            "game":{
                "bg":(40, 44, 52),
                "rect-bg":(33, 37, 43)
            }
        }
        
        self.screen = pygame.display.set_mode((800,800),pygame.RESIZABLE)
        self.width, self.height = self.screen.get_size()
        self.zoom = min(self.screen.get_size())/800

        self.Clock = pygame.time.Clock()

    def main(self, mainself):

        self.fps = self.Clock.get_fps()
        if self.fps != 0: self.speed = 60/self.fps
        else: self.speed = 0

        exec(f"mainself.Scene.{mainself.status}.Display.main(mainself)")

    def on_resize(self, mainself):

        self.width, self.height = self.screen.get_size()
        self.zoom = min(self.screen.get_size())/800

        exec(f"mainself.Scene.{mainself.status}.Display.on_resize(mainself)")