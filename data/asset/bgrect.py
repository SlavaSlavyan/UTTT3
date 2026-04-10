import pygame

BASE_SIZE = 600 # константа размера

class BgRect:
    '''Задний фон ввиде куба'''

    def __init__(self, mainself, size:float = 1):
        '''- **size**: множитель размера'''
        
        mainself.Log.write(f"Создан экземпляр спрайта задника.\nРазмер = {size}","DEBUG")
        
        # множитель размера
        self.size = size
        
        # генерируем
        self.resize(mainself)

    def draw(self, mainself):
        '''Отображение фигуры'''

        display = mainself.Display

        # изменяем размер фигуры если это нужно
        if self.size == 1:
            surface = self.surface

        else:
            surface = pygame.transform.scale(self.surface,
                                   (BASE_SIZE * display.zoom * self.size,
                                    BASE_SIZE * display.zoom * self.size)),
            surface = surface[0]
        
        # отрисовываем фигуру
        display.screen.blit(surface,
                      (display.width//2 - BASE_SIZE/2 * display.zoom * self.size,
                       display.height//2 - BASE_SIZE/2 * display.zoom * self.size))

    def resize(self, mainself):
        '''Генерация фигуры'''
        
        mainself.Log.write(f"Перерисовка спрайта задника")
        
        # создаём поверхность фигуры
        self.surface = pygame.Surface((BASE_SIZE * mainself.Display.zoom,
                                       BASE_SIZE * mainself.Display.zoom))
        
        # заливаем фигуру одним цветом
        self.surface.fill(mainself.Display.colors["game"]["rect-bg"])