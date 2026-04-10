import pygame

class Corner:
    '''Уголок выделения'''

    def __init__(self, mainself, angle:int, base_size:float = 1, color:tuple = "DEFAULT"):
        '''- **angle**: поворот фигуры
        - **base_size**: начальный множитель размера
        - **color**: цвет'''
        
        mainself.Log.write(f"Создан экземпляр спрайта уголка выделения клетки.\nПоворот = {angle}\nНачальный размер = {base_size}\nЦвет = {color}","DEBUG")
        
        self.base_size = base_size
        self.angle = angle
        
        # меняем цвет на кастомный если это нужно
        if color == "DEFAULT":
            self.color = mainself.Display.colors["game"]["select-corner"]
        else:
            self.color = color

        # генерируем
        self.resize(mainself)

    def draw(self, mainself, pos:tuple, rect_align:tuple, canvas:pygame.surface.Surface = "SCREEN"):
        '''Отображение фигуры
        - **pos**: позиция относительно центра
        - **rect_align**: решает с какого именно угла нужно отрисовать фигуру (относительно себя)
        - **canvas**: поверхность на которой будет нарисован обьект'''

        display = mainself.Display

        # создаём ссылку на поверхность и получаем её размеры
        if canvas == "SCREEN":
            canvas = display.screen
            center = (display.width//2,display.height//2)

        else:
            center = canvas.get_rect().center

        # расчитываем откуда надо будет начинать рисовать фигуру
        rect = (self.rect[0]*rect_align[0],self.rect[1]*rect_align[1])

        # отрисовываем фигуру
        canvas.blit(self.surface,(center[0] - rect[0] + pos[0]*display.zoom,
                             center[1] - rect[1] - pos[1]*display.zoom))

    def resize(self, mainself):
        '''Генерация фигуры'''
        
        mainself.Log.write(f"Перерисовка спрайта уголка выделения клетки.")

        # создаём поверхность
        self.surface = pygame.Surface((4, 4), pygame.SRCALPHA)

        # рисуем линии по пиксельно
        pygame.draw.line(self.surface, self.color,(0,0),(0,3))
        pygame.draw.line(self.surface, self.color,(0,0),(3,0))

        # приводим замер фигуры к нормальному
        self.surface = pygame.transform.scale(self.surface, (200 * self.base_size * mainself.Display.zoom,
                                                             200 * self.base_size * mainself.Display.zoom))
        
        # изменяем угол фигуры если это нужно
        if self.angle != 0:
            self.surface = pygame.transform.rotate(self.surface, self.angle)

        # получаем центр поверхности
        self.rect = self.surface.get_rect().size