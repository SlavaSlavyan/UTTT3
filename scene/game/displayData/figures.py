# ВАЖНО!!! запись ПЕРЕМЕННАЯ[i][j] нужна из-за того что если записать эту конструкцию в переменную, то она не скопирует ссылку на неё

SMALL_FIGURES_RESIZE_SPEED = 1/30 # скорость изменения размера маленьких клеток
BIG_FIGURES_RESIZE_SPEED = 1/45   # скорость изменения размера больших клеток

class Figures:
    '''Отрисовка фигур'''

    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса отображения фигур сцены Game.","DEBUG")
        
        # размеры маленьких фигур (двухмерный массив)
        self.small_figure_sizes = []

        # размеры больших фигур
        self.big_figure_sizes = []

        # заполняем массивы начальными значениями
        for i in range(9):
            self.small_figure_sizes.append([])

            for j in range(9):
                self.small_figure_sizes[i].append(0)
                self.big_figure_sizes.append(0)

    def main(self, mainself):
        '''Отрисовка всех фигур (и маленьких и больших)'''
        
        # прогон всех больших клеток
        for i in range(9):
            
            # прогон всех маленьких клеток внутри больших
            for j in range(9):
                
                # рисуем маленькие фигуры
                self.draw_small_figures(mainself,i,j)
                
                # обновляем размеры маленьких фигур
                self.new_small_figure_size(mainself,i,j)

            # рисуем большие фигуры
            self.draw_big_figures(mainself, i)
            
            # обновляем размеры больших фигур
            self.new_big_figure_size(mainself, i)
    
    def new_small_figure_size(self, mainself, i:int, j:int):
        '''Обновляет размер маленькой клетки
        - **i**: ID большой клетки
        - **j**: ID маленькой клетки'''

        scene = mainself.Scene.Game
        display = mainself.Display

        # получаем список всех клеток
        cells = scene.Logic.Game.cells

        # размеры всех маленьких клеток
        size = self.small_figure_sizes

        # если большая клетка не захвачена
        if None in cells[i] or len(set(cells[i])) != 1:
            
            if cells[i][j] == 0:
                        
                if size[i][j] < 1:
                    size[i][j] += SMALL_FIGURES_RESIZE_SPEED * display.speed
                    if size[i][j] > 1:
                        size[i][j] = 1
                
                return
            
            if cells[i][j] == 1:

                if size[i][j] > -1:
                    size[i][j] -= SMALL_FIGURES_RESIZE_SPEED * display.speed
                    if size[i][j] < -1:
                        size[i][j] = -1
            
                return

        # уменьшаем размер в других случаях

        if size[i][j] < 0:
            size[i][j] += SMALL_FIGURES_RESIZE_SPEED * display.speed
            if size[i][j] > 0:
                size[i][j] = 0

        if size[i][j] > 0:
            size[i][j] -= SMALL_FIGURES_RESIZE_SPEED * display.speed
            if size[i][j] < 0:
                size[i][j] = 0
    
    def draw_small_figures(self, mainself, i:int, j:int):
        '''Рисует маленькую фигуру
        - **i**: ID большой клетки
        - **j**: ID маленькой клетки'''

        scene = mainself.Scene.Game

        # отрисовываем только если значение не равно 0

        if self.small_figure_sizes[i][j] > 0:
            scene.SmallCircle.draw(mainself,(200*(i%3-1)+50*(j%3-1),
                                            -200*(i//3-1)-50*(j//3-1)),
                                            self.small_figure_sizes[i][j])
        
        if self.small_figure_sizes[i][j] < 0:
            scene.SmallCross.draw(mainself,(200*(i%3-1)+50*(j%3-1),
                                           -200*(i//3-1)-50*(j//3-1)),
                                           -self.small_figure_sizes[i][j])
    
    def new_big_figure_size(self, mainself, i:int):
        '''Обновляет размер большой клетки
        - **i**: ID большой клетки'''

        scene = mainself.Scene.Game
        display = mainself.Display

        # получаем список всех клеток
        cells = scene.Logic.Game.cells

        # размеры всех больших клеток
        size = self.big_figure_sizes

        # если клетка захвачена 0
        if all(x == 0 for x in cells[i]):
                    
            if size[i] < 1:
                size[i] += BIG_FIGURES_RESIZE_SPEED * display.speed
                if size[i] > 1:
                    size[i] = 1
        
        # если клетка захвачена X
        elif all(x == 1 for x in cells[i]):

            if size[i] > -1:
                size[i] -= BIG_FIGURES_RESIZE_SPEED * display.speed
                if size[i] < -1:
                    size[i] = -1
        
        # уменьшаем размер в других случаях
        else:

            if size[i] < 0:
                size[i] += BIG_FIGURES_RESIZE_SPEED * display.speed
                if size[i] > 0:
                    size[i] = 0

            if size[i] > 0:
                size[i] -= BIG_FIGURES_RESIZE_SPEED * display.speed
                if size[i] < 0:
                    size[i] = 0
    
    def draw_big_figures(self, mainself, i:int):
        '''Рисует большую фигуру
        - **i**: ID большой клетки'''

        scene = mainself.Scene.Game

        # отрисовываем только если значение не равно 0

        if self.big_figure_sizes[i] > 0:
            scene.BigCircle.draw(mainself,(200*(i%3-1),
                                            -200*(i//3-1)),
                                            self.big_figure_sizes[i])
        
        if self.big_figure_sizes[i] < 0:
            scene.BigCross.draw(mainself,(200*(i%3-1),
                                           -200*(i//3-1)),
                                           -self.big_figure_sizes[i])