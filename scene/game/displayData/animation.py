import pygame
import math

class Animation:

    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса отображения анимации сцены Game.","DEBUG")
        
        self.time = 1
        self.speed = -1

    def main(self, mainself):

        scene = mainself.Scene.Game
        most = max(mainself.Display.width, mainself.Display.height)
        
        time = self.time * self.time
        
        scene.Bg.size = 1 - time
        scene.Bg.draw(mainself)
        
        scene.LineHorizontal.draw(mainself,(most*time,100))
        scene.LineHorizontal.draw(mainself,(-most*time,-100))
        scene.LineVertical.draw(mainself,(-100,most*time))
        scene.LineVertical.draw(mainself,(100,-most*time))

        for y in range(-1,2):
            for x in range(-1,2):

                size = "DEFAULT"

                if not y and not x:
                    size = 1 - time

                scene.SmallCells.draw(mainself, (200*x + x*most*time,
                                                 200*y + y*most*time), size)

        scene.corners[0].draw(mainself,(-375-most*time,375+most*time),(0,0))
        scene.corners[1].draw(mainself,(-375-most*time,-375-most*time),(0,1))
        scene.corners[2].draw(mainself,(375+most*time,-375-most*time),(1,1))
        scene.corners[3].draw(mainself,(375+most*time,375+most*time),(1,0))
        
        self.time = self.time + self.speed/60*mainself.Display.speed