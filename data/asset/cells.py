import pygame

class Cells:

    def __init__(self, mainself, transparency:float = 1, size:int = 1, line_width:int = 5):
        
        mainself.Log.write(f"Создан экземпляр спрайта клеток.\nПрозрачность = {transparency}\nРазмер = {size}\nШирина линий = {line_width}","DEBUG")
        
        self.base_transparency = transparency
        self.base_size = size
        self.line_width = line_width

        self.resize(mainself)

    def draw(self, mainself, pos:tuple, size:float = "DEFAULT", transparency:float = "DEFAULT", canvas:pygame.surface.Surface = "SCREEN"):

        display = mainself.Display

        if canvas == "SCREEN":
            canvas = display.screen
            center = (display.width//2,display.height//2)

        else:
            center = canvas.get_rect().center

        if size != "DEFAULT":
            rect = (self.rect[0]*size,
                    self.rect[1]*size)
            surface = pygame.transform.smoothscale(self.surface, (rect[0]*2,rect[1]*2))
            
        else:
            rect = self.rect
            surface = self.surface
        
        if transparency != "DEFAULT" and transparency != self.base_transparency:
            
            if surface == self.surface:
                surface = self.surface.copy()
            
            surface.set_alpha(transparency*255)

        canvas.blit(surface,(center[0] - rect[0] + pos[0]*display.zoom,
                             center[1] - rect[1] - pos[1]*display.zoom))

    def resize(self, mainself):
        
        mainself.Log.write(f"Перерисовка спрайта клеток")

        self.surface = pygame.Surface((600 * self.base_size * mainself.Display.zoom,
                                       600 * self.base_size * mainself.Display.zoom),
                                       pygame.SRCALPHA)
        
        line = mainself.Asset.Line(mainself, width = self.line_width)
        
        line.draw(mainself,(0,100*self.base_size),self.surface)
        line.draw(mainself,(0,-100*self.base_size),self.surface)
        
        line.angle = 90
        line.resize(mainself)
        
        line.draw(mainself,(-100*self.base_size,0),self.surface)
        line.draw(mainself,(100*self.base_size,0),self.surface)

        self.rect = self.surface.get_rect().center

        self.surface.set_alpha(self.base_transparency*255)