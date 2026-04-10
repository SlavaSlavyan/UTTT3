import pygame

# константа размера задника
from data.asset.bgrect import BASE_SIZE as BS_BGRECT

class Cells:
    '''Клетки'''

    def __init__(self, mainself, transparency:float = 1, size:int = 1, line_width:int = 5):
        '''- **transparency**: базовая прозрачность
        - **size**: начальный множитель размера
        - **line_width**: ширина линий'''
        
        mainself.Log.write(f"Создан экземпляр спрайта клеток.\nПрозрачность = {transparency}\nРазмер = {size}\nШирина линий = {line_width}","DEBUG")
        
        self.base_transparency = transparency
        self.base_size = size
        self.line_width = line_width

        # генерируем
        self.resize(mainself)

    def draw(self, mainself, pos:tuple, size:float = "DEFAULT", transparency:float = "DEFAULT", canvas:pygame.surface.Surface = "SCREEN"):
        '''Отображение фигуры
        - **pos**: позиция относительно центра
        - **size**: множитель размера
        - **transparency**: прозрачность
        - **canvas**: поверхность на которой будет нарисован обьект'''

        display = mainself.Display

        # создаём ссылку на поверхность и получаем её размеры
        if canvas == "SCREEN":
            canvas = display.screen
            center = (display.width//2,display.height//2)

        else:
            center = canvas.get_rect().center

        # изменяем размер если это нужно
        if size != "DEFAULT":
            rect = (self.rect[0]*size,
                    self.rect[1]*size)
            surface = pygame.transform.smoothscale(self.surface, (rect[0]*2,rect[1]*2))
            
        else:
            rect = self.rect
            surface = self.surface
        
        # изменяем прозрачность если это нужно
        if transparency != "DEFAULT" and transparency != self.base_transparency:
            
            if surface == self.surface:
                surface = self.surface.copy()
            
            surface.set_alpha(transparency*255)

        # отрисовываем фигуру
        canvas.blit(surface,(center[0] - rect[0] + pos[0]*display.zoom,
                             center[1] - rect[1] - pos[1]*display.zoom))

    def resize(self, mainself):
        '''Генерация фигуры'''
        
        mainself.Log.write(f"Перерисовка спрайта клеток")

        # создаём поверхность
        self.surface = pygame.Surface((BS_BGRECT * self.base_size * mainself.Display.zoom,
                                       BS_BGRECT * self.base_size * mainself.Display.zoom),
                                       pygame.SRCALPHA)
        
        # создаём экземпляр линии
        line = mainself.Asset.Line(mainself, width = self.line_width)
        
        # рисуем горизонтальные линии
        line.draw(mainself,(0,100*self.base_size),self.surface)
        line.draw(mainself,(0,-100*self.base_size),self.surface)
        
        # поворачиваем поверхность
        line.angle = 90
        line.resize(mainself)
        
        # рисуем вертикальные линии
        line.draw(mainself,(-100*self.base_size,0),self.surface)
        line.draw(mainself,(100*self.base_size,0),self.surface)
        
        # получаем центр поверхности
        self.rect = self.surface.get_rect().center
        
        # задаём начальное значение прозрачности
        self.surface.set_alpha(self.base_transparency*255)