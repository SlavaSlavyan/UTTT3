STATIC_TRANSPARENCY_VALUE = 0.25 # статическое значение прозрачности клетки в котором она находится большую часть времени
FADE_SPEED = 1/30                # скорость изменения прозрачности
VANISHING_SPEED = 1/45           # скорость изменения прозрачности при захвате клетки

class Cells:
    '''Отрисовка маленьких клеток'''
    
    def __init__(self,mainself):
        
        mainself.Log.write("Инициализация класса отображения клеток сцены Game.","DEBUG")
        
        # прозрачность каждой клетки
        self.cells_transparency = []
        
        # заполняем массив начальными данными
        for i in range(9):
            self.cells_transparency.append(STATIC_TRANSPARENCY_VALUE)
    
    def main(self, mainself):
        '''Как же я заебался на самом деле это всё описывать...'''
        
        scene = mainself.Scene.Game
        
        # проход по каждой клетке
        for i in range(9):
            
            # если прозрачность не равна нулю
            if self.cells_transparency[i] != 0:
                
                # отрисовываем клетку
                scene.SmallCells.draw(mainself, (200*(i%3-1),
                                                -200*(i//3-1)), 
                                    transparency=self.cells_transparency[i])

            # новые значения прозрачности
            self.new_transparency(mainself,i)
    
    def new_transparency(self, mainself, i:int):
        '''Изменяет значение прозрачности клетки
        - **i**: ID клетки'''

        # все значения клеток
        cells = mainself.Scene.Game.Logic.Game.cells
        
        # если клетка не захвачена
        if None in cells[i] or len(set(cells[i])) != 1:
            
            # если клетка выбранна
            if mainself.Scene.Game.Logic.Game.selected_cell == i:
                
                if self.cells_transparency[i] < 1:
                    self.cells_transparency[i] += FADE_SPEED * mainself.Display.speed
                
                if self.cells_transparency[i] > 1:
                    self.cells_transparency[i] = 1
                
                return None

            # иначе прозрачность стремится к статическому значению
                
            if self.cells_transparency[i] > STATIC_TRANSPARENCY_VALUE:
                self.cells_transparency[i] -= FADE_SPEED * mainself.Display.speed
            
            if self.cells_transparency[i] < STATIC_TRANSPARENCY_VALUE:
                self.cells_transparency[i] += FADE_SPEED * mainself.Display.speed

                if self.cells_transparency[i] > STATIC_TRANSPARENCY_VALUE:
                    self.cells_transparency[i] = STATIC_TRANSPARENCY_VALUE

            return None

        # если клетка захваченна, она стремится к полному исчезновению
        
        if self.cells_transparency[i] > 0:
            self.cells_transparency[i] -= VANISHING_SPEED * mainself.Display.speed
        
        if self.cells_transparency[i] < 0:
            self.cells_transparency[i] = 0