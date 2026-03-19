import pygame

class BgRect:

    def __init__(self, mainself, size:float = 1):
        
        self.size = size
        
        self.resize(mainself)

    def draw(self, mainself):

        display = mainself.Display

        if self.size == 1:
            surface = self.surface

        else:
            surface = pygame.transform.scale(self.surface,
                                   (600 * display.zoom * self.size,
                                    600 * display.zoom * self.size)),
            surface = surface[0]
        
        display.screen.blit(surface,
                      (display.width//2 - 300 * display.zoom * self.size,
                       display.height//2 - 300 * display.zoom * self.size))

    def resize(self, mainself):
        
        self.surface = pygame.Surface((600 * mainself.Display.zoom,
                                       600 * mainself.Display.zoom))
        
        self.surface.fill(mainself.Display.colors["game"]["rect-bg"])