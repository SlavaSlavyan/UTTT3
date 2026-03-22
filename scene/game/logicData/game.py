class Game:
    
    def __init__(self, mainself):
        
        self.selected_cell = None
        self.player = 0

        self.cells = []

        for i in range(9):
            self.cells.append([])

            for j in range(9):
                self.cells[i].append(None)
    
    def main(self, mainself):
        
        if self.selected_cell == None:
            self.check_big_selected_cell(mainself, mainself.Scene.Game.Logic.Select.select_big_cell(mainself))

        else:
            self.check_small_selected_cell(mainself, mainself.Scene.Game.Logic.Select.select_small_cell(mainself))
    
    def check_big_selected_cell(self,mainself,cell):
        
        if cell != None:

            if None in self.cells[cell]:

                self.selected_cell = cell

                return True
        
            return False
    
    def check_small_selected_cell(self, mainself, cell):

        if cell != None:

            if self.cells[self.selected_cell][cell] == None:

                self.cells[self.selected_cell][cell] = self.player

                result = self.check_capture(mainself)

                if result:
                    for i in range(9):
                        self.cells[self.selected_cell][i] = self.player

                if self.player:
                    self.player = 0
                else:
                    self.player = 1
                
                result = self.check_big_selected_cell(mainself,cell)
                
                if not result:
                    self.selected_cell = None
    
    def check_capture(self, mainself):

        cell = self.cells[self.selected_cell]
        
        for i in range(3):

            if cell[3*i] == self.player and cell[1+3*i] == self.player and cell[2+3*i] == self.player:
                return True
            
            if cell[i] == self.player and cell[3+i] == self.player and cell[6+i] == self.player:
                return True
        
        if cell[0] == self.player and cell[4] == self.player and cell[8] == self.player:
            return True
        
        if cell[2] == self.player and cell[4] == self.player and cell[6] == self.player:
            return True
        
        return False