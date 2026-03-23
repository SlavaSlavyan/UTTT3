class Game:
    
    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса логики игры сцены Game. (ну типо да, логика самой игры)","DEBUG")
        
        self.selected_cell = None
        self.player = 0

        self.cells = []

        for i in range(9):
            self.cells.append([])

            for j in range(9):
                self.cells[i].append(None)
    
    def main(self, mainself):
        
        mainself.Log.write("Запуск функции логики игры.")
        
        if self.selected_cell == None:
            self.check_big_selected_cell(mainself, mainself.Scene.Game.Logic.Select.select_big_cell(mainself))

        else:
            self.check_small_selected_cell(mainself, mainself.Scene.Game.Logic.Select.select_small_cell(mainself))
    
    def check_big_selected_cell(self,mainself,cell):
        
        mainself.Log.write(f"Проверка выбранной большой клетки. Cell = {cell}")
        
        if cell != None:

            if None in self.cells[cell]:

                self.selected_cell = cell
                
                mainself.Log.write(f"Выбранна клетка {cell}")
                
                return True

            mainself.Log.write("Клетка занята.")
            return False
        
        mainself.Log.write("Клетка не выбрана.")
    
    def check_small_selected_cell(self, mainself, cell):
        
        mainself.Log.write(f"Проверка выбранной маленькой клетки. Cell = {cell}")

        if cell != None:

            if self.cells[self.selected_cell][cell] == None:

                self.cells[self.selected_cell][cell] = self.player
                mainself.Log.write(f"Данные клетки {self.selected_cell} были перезаписанны.\n{self.cells[self.selected_cell]}")

                result = self.check_capture(mainself)

                if result:
                    mainself.Log.write(f"Клетка захвачена.")
                    for i in range(9):
                        self.cells[self.selected_cell][i] = self.player
                    mainself.Log.write(f"Данные клетки {self.selected_cell} были перезаписанны.\n{self.cells[self.selected_cell]}")

                if self.player:
                    self.player = 0
                else:
                    self.player = 1
                mainself.Log.write(f"Смена игрока ({self.player}).")
                
                mainself.Log.write(f"Выбор следующей клетки.")
                result = self.check_big_selected_cell(mainself,cell)
                
                if not result:
                    self.selected_cell = None
                    mainself.Log.write(f"Клетка не выбрана.")
                    
            else:
                mainself.Log.write("Клетка занята.")
                
        else:
            mainself.Log.write("Клетка не выбрана.")
    
    def check_capture(self, mainself):
        
        mainself.Log.write(f"Проверка захвата клетки.")

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
        
        mainself.Log.write(f"Клетка не захвачена.")
        return False