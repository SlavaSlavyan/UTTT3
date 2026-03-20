import pygame

from scene.game.displayData.cells import Cells

class Game:
    
    def __init__(self, mainself):
        
        self.Cells = Cells(mainself)
    
    def main(self, mainself):
        
        scene = mainself.Scene.Game
        
        scene.Bg.draw(mainself)
        self.Cells.main(mainself)
        
        scene.Select.draw(mainself, "LOCAL", "LOCAL")