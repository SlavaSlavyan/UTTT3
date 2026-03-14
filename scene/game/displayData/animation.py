import pygame
import math

class Animation:

    def __init__(self, mainself):
        
        self.t = 1
        self.speed = -1.5

    def main(self, mainself):

        s = mainself.Scene.Game

        s.Item.BgRect.resize(mainself, math.cos(self.t/2*math.pi))
        s.Item.BgRect.draw(mainself)

        self.t += self.speed/100 * mainself.Display.speed