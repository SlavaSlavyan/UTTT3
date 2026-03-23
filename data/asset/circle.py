import pygame

class Circle:

    def __init__(self, mainself, size:float = 1):
        
        mainself.Log.write(f"Создан экземпляр спрайта нолика.\nРазмер = {size}","DEBUG")
        
        self.base_size = size
        
        self.resize(mainself)

    def draw(self,mainself, pos:tuple, size:float = 1, transparency:float = 1):
        
        display = mainself.Display

        if size != 1:
            rect = (self.rect[0]*size,
                    self.rect[1]*size)
            surface = pygame.transform.smoothscale(self.surface, (rect[0]*2,rect[1]*2))
            
        else:
            rect = self.rect
            surface = self.surface
        
        if transparency != 1:
            
            if surface == self.surface:
                surface = self.surface.copy()
            
            surface.set_alpha(transparency*255)
        
        center = (display.width//2,display.height//2)

        display.screen.blit(surface,(center[0] - rect[0] + pos[0]*display.zoom,
                             center[1] - rect[1] - pos[1]*display.zoom))

    def resize(self,mainself):
        
        mainself.Log.write(f"Перерисовка спрайта нолика")
        
        self.surface = pygame.Surface((200 * self.base_size * mainself.Display.zoom,
                                       200 * self.base_size * mainself.Display.zoom),
                                       pygame.SRCALPHA)
        
        self.rect = self.surface.get_rect().center
        
        pygame.draw.circle(self.surface,mainself.Display.colors["game"]["circle"],
                           self.rect,100*self.base_size*mainself.Display.zoom)
        
        pygame.draw.circle(self.surface,mainself.Display.colors["game"]["rect-bg"],
                           self.rect,75*self.base_size*mainself.Display.zoom)