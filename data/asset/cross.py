import pygame

class Cross:

    def __init__(self, mainself, size:float = 1):
        
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
        
        line = pygame.Surface((1,3),pygame.SRCALPHA)

        line.fill(mainself.Display.colors["game"]["cross"])

        line = pygame.transform.scale(line, (200/3 * self.base_size * mainself.Display.zoom,
                                                             200 * self.base_size * mainself.Display.zoom))
        
        self.surface = pygame.transform.rotate(line, 45)

        line = pygame.transform.rotate(line, -45)

        self.surface.blit(line,(0,0))
        
        self.rect = self.surface.get_rect().center