import pygame

RESIZE_SPEED = 1/30 # скорость изменения размера 

class Select:
    
    def __init__(self, mainself, base_size:float = 1, color:tuple = "DEFAULT"):
        '''- **base_size**: начальный множитель размера
        - **color**: цвет'''
        
        mainself.Log.write(f"Создан экземпляр спрайта выбора клетки.\nБазовый размер = {base_size}\nЦвет = {color}","DEBUG")
        
        self.base_size = base_size
        self.color = color
        
        self.pos = [0,0]          # позиция на экране
        self.offset = [0,0]       # смещение относительно позиции
        self.size = 1             # локальный множитель размера
        self.selected_cell = None # выбранная клетка
        
        # генерируем
        self.resize(mainself)
    
    def draw(self, mainself, pos:int = "LOCAL", size:float = "DEFAULT", transparency:float = 1):
        '''Отображение фигуры.\n
        Аргумент **LOCAL** обозначает взятие локальных переменных внутри класса
        - **pos**: позиция относительно центра
        - **size**: множитель размера
        - **transparency**: прозрачность'''
        
        display = mainself.Display
        
        # изменяем размер если это нужно
        if size == "DEFAULT":
            
            surface = self.surface
            size = self.base_size
            rect = self.rect

        else: 
            
            if size == "LOCAL":
                size = self.size
                
            surface = pygame.transform.smoothscale(self.surface,
                                   (750 * display.zoom * size * self.base_size,
                                    750 * display.zoom * size * self.base_size)),
            surface = surface[0]
            
            rect = surface.get_rect().center
        
        # изменяем прозрачность если это нужно
        if transparency != 1:
            
            if surface == self.surface:
                surface = self.surface.copy()
            
            surface.set_alpha(transparency*255)
        
        # берём локальную позицию при соответствующем аргументе
        if pos == "LOCAL":
            pos = (self.pos[0] + self.offset[0], self.pos[1] + self.offset[1])
        
        # отрисовываем фигуру
        display.screen.blit(surface,
                      (display.width//2 - rect[0] + pos[0]*display.zoom,
                       display.height//2 - rect[1] - pos[1]*display.zoom))
        
        # запускаем логику выделения
        self.logic(mainself)
    
    def resize(self, mainself):
        '''Генерация фигуры'''
        
        mainself.Log.write(f"Перерисовка спрайта выбора клетки")
        
        # создаём поверхность
        self.surface = pygame.Surface((750 * mainself.Display.zoom,
                                       750 * mainself.Display.zoom),
                                       pygame.SRCALPHA)
        
        # массив для углов
        corners = []
        
        # создаём 4 экземпляра углов
        for i in range(4):
            corners.append(mainself.Asset.Corner(mainself, 90*i, color = self.color))

        # отрисовываем их на поверхности
        corners[0].draw(mainself,(-375,375),(0,0), self.surface)
        corners[1].draw(mainself,(-375,-375),(0,1), self.surface)
        corners[2].draw(mainself,(375,-375),(1,1), self.surface)
        corners[3].draw(mainself,(375,375),(1,0), self.surface)
        
        # изменяем начальный размер
        self.surface = pygame.transform.scale(self.surface, (750 * self.base_size * mainself.Display.zoom,
                                                             750 * self.base_size * mainself.Display.zoom))
        
        # получаем центр поверхности
        self.rect = self.surface.get_rect().center

    def logic(self, mainself):
        '''Логика отображения выделения'''
        
        # если выбранная клетка была обновленна задаём новую позицию
        if self.selected_cell != mainself.Scene.Game.Logic.Game.selected_cell:
            self.newpos(mainself)

        # задаём новый размер
        self.newsize(mainself)
        
        # уменьшаем смещение каждую секунду
        self.offset[0] /= 1 + 0.1 * mainself.Display.speed
        self.offset[1] /= 1 + 0.1 * mainself.Display.speed
    
    def newpos(self,mainself):
        '''Вычисление новой позиции'''
        
        # записываем новую выбранную клетку
        self.selected_cell = mainself.Scene.Game.Logic.Game.selected_cell
        
        # получаем нынешнее положение в пространстве
        now = (self.pos[0] + self.offset[0], self.pos[1] + self.offset[1])
        
        # получаем позицию новой клетки
        if self.selected_cell == None: 
            x, y = 0, 0
        else:
            x = (self.selected_cell%3) - 1
            y = (self.selected_cell//3) - 1
        
        # записываем в локальную переменную
        self.pos = [200*x,200*-y]

        # обновляем смещение
        self.offset = [now[0]-self.pos[0],now[1]-self.pos[1]]
        
    def newsize(self,mainself):
        '''Вычисление размера'''
        
        # если клетка не выбранна, то выделение должно увеличиваться
        if self.selected_cell == None:
            
            if self.size < 1:
                self.size += RESIZE_SPEED * mainself.Display.speed
            
            if self.size > 1:
                self.size = 1
        
        # иначе уменьшаем
        else:
            
            if self.size > 0.25:
                self.size -= RESIZE_SPEED * mainself.Display.speed
            
            if self.size < 0.25:
                self.size = 0.25