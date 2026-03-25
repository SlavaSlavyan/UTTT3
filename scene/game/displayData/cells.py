import pygame

class Cells:
    
    def __init__(self,mainself):
        
        mainself.Log.write("Инициализация класса отображения клеток сцены Game.","DEBUG")
        
        self.cells_transparency = []
        
        for i in range(9):
            self.cells_transparency.append(0.25)
    
    def main(self, mainself):
        
        scene = mainself.Scene.Game
        
        for i in range(9):
            
            if self.cells_transparency[i] != 0:

                scene.SmallCells.draw(mainself, (200*(i%3-1),
                                                -200*(i//3-1)), 
                                    transparency=self.cells_transparency[i])

            self.new_size(mainself,self.cells_transparency,i)
    
    def new_size(self, mainself, cell, i):

        cells = mainself.Scene.Game.Logic.Game.cells
        
        if None in cells[i] or len(set(cells[i])) != 1:
            
            if mainself.Scene.Game.Logic.Game.selected_cell == i:
                
                if cell[i] < 1:
                    cell[i] += 1/30 * mainself.Display.speed
                
                if cell[i] > 1:
                    cell[i] = 1
                
                return None

                
            if cell[i] > 0.25:
                cell[i] -= 1/30 * mainself.Display.speed
            
            if cell[i] < 0.25:
                cell[i] += 1/30 * mainself.Display.speed

                if cell[i] > 0.25:
                    cell[i] = 0.25

            return None

        if cell[i] > 0:
            cell[i] -= 1/45 * mainself.Display.speed
        
        if cell[i] < 0:
            cell[i] = 0