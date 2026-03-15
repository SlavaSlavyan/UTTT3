import pygame
import math

class Animation:

    def __init__(self, mainself):
        
        self.t = 1
        self.speed = -1.5

    def main(self, mainself):

        s = mainself.Scene.Game
        t = 3 * self.t ** 2 - 2 * self.t ** 3
        m = max(mainself.Display.width, mainself.Display.height)

        s.Item.BgRect.draw(mainself, -t+1)  

        s.Item.Line.draw(mainself,(m*t,-100))
        s.Item.Line.draw(mainself,(m*-t,100))
        s.Item.Line.draw(mainself,(-100,m*-t),90)
        s.Item.Line.draw(mainself,(100,m*t),90)

        for y in range(-1,2): 
            for x in range(-1,2):

                if (not x and not y):
                    s.Item.Cells.draw(mainself,(0,0),0.25,-t+1,"SMALL")
                    continue

                s.Item.Cells.draw(mainself,(200*x+m*t*x,200*y+m*t*y),0.25,-t+1,"SMALL")

        self.t += self.speed/100 * mainself.Display.speed