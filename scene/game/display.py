import pygame

from scene.game.displayData.animation import Animation

class Display:

    def __init__(self, mainself):

        self.Animation = Animation(mainself)

    def main(self, mainself):

        scene = mainself.Scene.Game

        mainself.Display.screen.fill(mainself.Display.colors["game"]["bg"])
        
        if scene.status == 0:
            
            self.Animation.main(mainself)
            
            if self.Animation.time <= 0:
                
                scene.status = 1

    def on_resize(self, mainself):

        scene = mainself.Scene.Game
        
        scene.Bg.resize(mainself)
        
        if scene.status == 0:
            
            scene.LineHorizontal.resize(mainself)
            scene.LineVertical.resize(mainself)