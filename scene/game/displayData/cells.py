import pygame

class Cells:
    
    def __init__(self,mainself):
        
        mainself.Log.write("Инициализация класса отображения клеток сцены Game.","DEBUG")
        
        self.cells_transparency = []
        
        for i in range(9):
            self.cells_transparency.append(0.25)
    
    def main(self, mainself):
        
        scene = mainself.Scene.Game
        
        for y in range(3):
            for x in range(3):

                scene.SmallCells.draw(mainself, (200*(x-1),
                                                 -200*(y-1)), 
                                      transparency=self.cells_transparency[x + 3*y])
                
                if scene.Logic.Game.selected_cell == x + 3*y:
                    
                    if self.cells_transparency[x + 3*y] < 1:
                        self.cells_transparency[x + 3*y] += 1/30 * mainself.Display.speed
                    
                    if self.cells_transparency[x + 3*y] > 1:
                        self.cells_transparency[x + 3*y] = 1

                else:
                    
                    if self.cells_transparency[x + 3*y] > 0.25:
                        self.cells_transparency[x + 3*y] -= 1/30 * mainself.Display.speed
                    
                    if self.cells_transparency[x + 3*y] < 0.25:
                        self.cells_transparency[x + 3*y] = 0.25