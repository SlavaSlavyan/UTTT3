import pygame

from scene.game.displayData.animation import Animation
from scene.game.displayData.game import Game

class Display:

    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса отображения сцены Game.","DEBUG")

        self.Animation = Animation(mainself)
        self.Game = Game(mainself)

    def main(self, mainself):

        scene = mainself.Scene.Game

        mainself.Display.screen.fill(mainself.Display.colors["game"]["bg"])
        
        if scene.status == 0:
            
            self.Animation.main(mainself)
            
            if self.Animation.time <= 0:
                
                mainself.Log.write("Новый статус сцены Game. (1)")
                
                scene.status = 1
                
                scene.Select = mainself.Asset.Select(mainself)
                scene.Selecting0 = mainself.Asset.Select(mainself,0.25,mainself.Display.colors["game"]["circle"])
                scene.SelectingX = mainself.Asset.Select(mainself,0.25,mainself.Display.colors["game"]["cross"])
                scene.UnablSelecting = mainself.Asset.Select(mainself,0.25,mainself.Display.colors["game"]["unavailable"])
                scene.SmallCircle = mainself.Asset.Circle(mainself,0.20)
                scene.SmallCross = mainself.Asset.Cross(mainself,0.20)
                scene.BigCircle = mainself.Asset.Circle(mainself,0.75)
                scene.BigCross = mainself.Asset.Cross(mainself,0.75)

                self.on_resize(mainself)

        if scene.status == 1:
            
            self.Game.main(mainself)

    def on_resize(self, mainself):
        
        mainself.Log.write("Перерисовка сцены Game.")

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
            scene.Selecting0.resize(mainself)
            scene.SelectingX.resize(mainself)
            scene.UnablSelecting.resize(mainself)
            scene.SmallCircle.resize(mainself)
            scene.SmallCross.resize(mainself)
            scene.BigCircle.resize(mainself)
            scene.BigCross.resize(mainself)