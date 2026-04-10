import pygame

class Label:
    '''Табличка со строкой'''

    def __init__(self, mainself, size:tuple, string:str, color:tuple, outline_width:int = 30, font_size:int = 50):
        '''- **size**: размеры прямоугольника
        - **string**: строчка на табличке
        - **color**: цвет
        - **outline_width**: ширина границы
        - **font_size**: размер шрифта'''
        
        mainself.Log.write(f"Создан экземпляр спрайта таблички.\nРазмер = {size}\nСтрока = {string}\nЦвет = {color}\nШирина границы = {outline_width}\nРазмер шрифта = {font_size}","DEBUG")
        
        self.size = size
        self.string = string
        self.color = color
        self.outline_width = outline_width
        self.font_size = font_size
        
        # генерируем
        self.resize(mainself)

    def draw(self, mainself, size:float):
        '''Отображение фигуры
        - **size**: множитель размера'''

        display = mainself.Display

        # меняем размер фигуры
        surface = pygame.transform.scale(self.surface,
                                        (self.rect[0]*2 * size,
                                         self.rect[1]*2 * size)),
        
        surface = surface[0]

        rect = surface.get_rect().center
        
        # отрисовываем фигуру
        display.screen.blit(surface,
                      (display.width//2 - rect[0],
                       display.height//2 - rect[1]))

    def resize(self, mainself):
        '''Генерация фигуры'''
        
        mainself.Log.write(f"Перерисовка спрайта задника")
        
        # создаём поверхность фигуры
        self.surface = pygame.Surface((self.size[0] * mainself.Display.zoom,
                                       self.size[1] * mainself.Display.zoom))
        
        # делаем контур
        self.surface.fill(self.color)

        # получаем центр поверхности
        self.rect = self.surface.get_rect().center

        # делаем поверхность поменьше для создания контура
        surface = pygame.Surface(((self.size[0] - self.outline_width*2) * mainself.Display.zoom,
                                  (self.size[1] - self.outline_width*2) * mainself.Display.zoom))

        surface.fill(mainself.Display.colors["game"]["rect-bg"])

        # отрисовываем контур
        self.surface.blit(surface, (self.rect[0] - surface.get_rect().centerx,
                                    self.rect[1] - surface.get_rect().centery))
        
        # создаём текст
        font = pygame.font.Font("data\\font\\base.ttf", round(self.font_size * mainself.Display.zoom))

        text = font.render(self.string, True, mainself.Display.colors["global"]["debug-text"])

        # отрисовываем текст
        self.surface.blit(text, (self.rect[0] - text.get_rect().centerx,
                                    self.rect[1] - text.get_rect().centery))