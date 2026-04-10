import pygame

class Circle:
    '''Нолик'''

    def __init__(self, mainself, size:float = 1):
        '''- **size**: множитель размера'''
        
        mainself.Log.write(f"Создан экземпляр спрайта нолика.\nРазмер = {size}","DEBUG")
        
        self.base_size = size
        
        # генерируем
        self.resize(mainself)

    def draw(self, mainself, pos:tuple, size:float = 1, transparency:float = 1):
        '''Отображение фигуры
        - **pos**: позиция относительно центра
        - **size**: множитель размера
        - **transparency**: прозрачность'''
        
        display = mainself.Display

        # изменяем размер если это нужно
        if size != 1:
            rect = (self.rect[0]*size,
                    self.rect[1]*size)
            surface = pygame.transform.smoothscale(self.surface, (rect[0]*2,rect[1]*2))
            
        else:
            rect = self.rect
            surface = self.surface
        
        # изменяем прозрачность если это нужно
        if transparency != 1:
            
            if surface == self.surface:
                surface = self.surface.copy()
            
            surface.set_alpha(transparency*255)
        
        # получаем центр экрана
        center = (display.width//2,display.height//2)

        # отрисовываем фигуру
        display.screen.blit(surface,(center[0] - rect[0] + pos[0]*display.zoom,
                             center[1] - rect[1] - pos[1]*display.zoom))

    def resize(self,mainself):
        '''Генерация фигуры'''
        
        mainself.Log.write(f"Перерисовка спрайта нолика")
        
        # создаём поверхность
        self.surface = pygame.Surface((200 * self.base_size * mainself.Display.zoom,
                                       200 * self.base_size * mainself.Display.zoom),
                                       pygame.SRCALPHA)
        
        # получаем центр поверхности
        self.rect = self.surface.get_rect().center
        
        # рисуем круги
        pygame.draw.circle(self.surface,mainself.Display.colors["game"]["circle"],
                           self.rect,100*self.base_size*mainself.Display.zoom)
        
        pygame.draw.circle(self.surface,mainself.Display.colors["game"]["rect-bg"],
                           self.rect,75*self.base_size*mainself.Display.zoom)