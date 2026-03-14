import pygame

from scene.game.displayData.animation import Animation

class Display:

    def __init__(self, mainself):
        
        self.colors = mainself.Display.colors["game"]

        self.Animation = Animation(mainself)

    def main(self, mainself):

        s = mainself.Scene.Game

        mainself.Display.screen.fill(self.colors["bg"])

        if s.status == 0:
            
            self.Animation.main(mainself)

            if self.Animation.t <= 0:

                s.status = 1

    def on_resize(self, mainself):

        s = mainself.Scene.Game

        s.Item.BgRect.resize(mainself)