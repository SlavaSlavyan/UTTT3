import pygame

# константа размера задника
from data.asset.bgrect import BASE_SIZE as BS_BGRECT

class Line:
    '''Линия'''

    def __init__(self, mainself, angle:int = 0, width:int = 5):
        '''- **angle**: поворот фигуры
        - **width**: ширина линии'''
        
        mainself.Log.write(f"Создан экземпляр спрайта линии.\nПоворот = {angle}\nШирина = {width}","DEBUG")
        
        self.angle = angle
        self.width = width
        
        # генерируем
        self.resize(mainself)

    def draw(self, mainself, pos:tuple, canvas:pygame.surface.Surface = "SCREEN"):
        '''Отображение фигуры
        - **pos**: позиция относительно центра
        - **canvas**: поверхность на которой будет нарисован обьект'''

        display = mainself.Display

        # создаём ссылку на поверхность и получаем её размеры
        if canvas == "SCREEN":
            canvas = display.screen
            center = (display.width//2,display.height//2)

        else:
            center = canvas.get_rect().center
        
        # отрисовываем фигуру
        canvas.blit(self.surface,(center[0] - self.rect[0] + pos[0]*display.zoom,
                             center[1] - self.rect[1] - pos[1]*display.zoom))

    def resize(self, mainself):
        '''Генерация фигуры'''
        
        mainself.Log.write(f"Перерисовка спрайта линии")

        # создаём поверхность
        self.surface = pygame.Surface((BS_BGRECT*mainself.Display.zoom,
                                       self.width*mainself.Display.zoom))
        
        # заливаем одним цветом
        self.surface.fill(mainself.Display.colors["game"]["line"])
        
        # изменяем угол линии если это нужно
        if self.angle != 0:
            self.surface = pygame.transform.rotate(self.surface,self.angle)
        
        # получаем центр поверхности
        self.rect = self.surface.get_rect().center