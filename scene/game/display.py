import pygame

from scene.game.displayData.animation import Animation
from scene.game.displayData.game import Game

class Display:

    def __init__(self, mainself):

        self.Animation = Animation(mainself)
        self.Game = Game(mainself)

    def main(self, mainself):

        scene = mainself.Scene.Game

        mainself.Display.screen.fill(mainself.Display.colors["game"]["bg"])
        
        if scene.status == 0:
            
            self.Animation.main(mainself)
            
            if self.Animation.time <= 0:
                
                scene.status = 1
                
                del scene.LineHorizontal, scene.LineVertical
                
                scene.Select = mainself.Asset.Select(mainself)

                self.on_resize(mainself)

        if scene.status == 1:
            
            self.Game.main(mainself)

    def on_resize(self, mainself):

        scene = mainself.Scene.Game
        
        scene.Bg.resize(mainself)
        scene.SmallCells.resize(mainself)
        
        if scene.status == 0:
            
            scene.LineHorizontal.resize(mainself)
            scene.LineVertical.resize(mainself)
            
            for i in range(4):
                scene.corners[i].resize(mainself)
        
        if scene.status == 1:
            
            cells = mainself.Asset.Cells(mainself)
            cells.draw(mainself,(0,0), canvas=scene.Bg.surface)
            
            scene.Select.resize(mainself)