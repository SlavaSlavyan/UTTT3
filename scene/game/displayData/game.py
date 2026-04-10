from scene.game.displayData.cells import Cells
from scene.game.displayData.figures import Figures
from scene.game.displayData.selecting import Selecting

class Game:
    '''Класс отображения ИГРЫ'''
    
    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса отображения игры сцены Game.","DEBUG")
        
        self.Cells = Cells(mainself)         # отрисовка клеток
        self.Figures = Figures(mainself)     # отрисовка фигур
        self.Selecting = Selecting(mainself) # отрисовка выбираемых клеток
    
    def main(self, mainself):
        '''Рисуем основное время игры'''
        
        scene = mainself.Scene.Game
        
        # рисуем задний фон
        scene.Bg.draw(mainself)

        # рисуем маленькие клетки
        self.Cells.main(mainself)
        
        # рисуем фигуры 
        self.Figures.main(mainself)

        # рисуем выбор клеток если мы всё ещё в игре
        if scene.status == 1:
            self.Selecting.main(mainself)

        # рисуем выбранную большую клетку
        scene.Select.draw(mainself, "LOCAL", "LOCAL")