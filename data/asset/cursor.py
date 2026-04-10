import pygame

TRANSPARENCY_SPEED = 1/15 # скорость изменения прозрачности курсора

class Cursor:
    '''Мышка'''
    
    def __init__(self, mainself):
        
        mainself.Log.write(f"Создан экземпляр спрайта курсора.","DEBUG")
        
        # множитель прозрачности
        self.transparency = 1
        
        # генерируем
        self.resize(mainself)
    
    def draw(self, mainself):
        '''Отображение фигуры'''

        # изменяем прозрачность если это нужно
        if self.transparency != 1:
            
            surface = self.surface.copy()
            surface.set_alpha(self.transparency*255)
        
        else:
            surface = self.surface
        
        # отрисовываем фигуру если она не прозрачна
        if self.transparency != 0:
            mainself.Display.screen.blit(surface, mainself.Event.Mouse.pos)
        
        # запускаем логику курсора
        self.logic(mainself)
    
    def resize(self, mainself):
        '''Генерация фигуры'''
        
        mainself.Log.write(f"Перерисовка спрайта курсора")
        
        # создаём поверхность фигуры
        self.surface = pygame.Surface((10,10),pygame.SRCALPHA)
        
        # создаём точки треугольника
        points = [(0,0),(9,0),(0,9)]
        
        # отрисовываем треугольник
        pygame.draw.polygon(self.surface,mainself.Display.colors["global"]["cursor"],points)
    
    def logic(self, mainself):
        '''Логика отображения курсора'''

        # повышаем прозрачность если режим управления - мышь
        if mainself.Event.mode == "MOUSE":
            
            if self.transparency < 1:
                self.transparency += TRANSPARENCY_SPEED * mainself.Display.speed
            
            if self.transparency > 1:
                self.transparency = 1
        
        # иначе понижаем
        else:
            
            if self.transparency > 0:
                self.transparency -= TRANSPARENCY_SPEED * mainself.Display.speed
            
            if self.transparency < 0:
                self.transparency = 0