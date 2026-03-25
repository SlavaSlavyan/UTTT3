import pygame

from scene.game.displayData.cells import Cells
from scene.game.displayData.figures import Figures
from scene.game.displayData.selecting import Selecting

class Game:
    
    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса отображения игры сцены Game.","DEBUG")
        
        self.Cells = Cells(mainself)
        self.Figures = Figures(mainself)
        self.Selecting = Selecting(mainself)
    
    def main(self, mainself):
        
        scene = mainself.Scene.Game
        
        scene.Bg.draw(mainself)

        self.Cells.main(mainself)
        
        self.Figures.main(mainself)
        self.Selecting.main(mainself)

        scene.Select.draw(mainself, "LOCAL", "LOCAL")