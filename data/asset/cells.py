import pygame

class Cells:

    def __init__(self, mainself, transparency:float = 1, size:int = 1, line_width:int = 5):
        
        self.transparency = transparency
        self.size = size

    def draw(self, mainself, pos:tuple, size:float = 1, canvas:pygame.surface.Surface = "SCREEN"):

        d = mainself.Display

        if canvas == "SCREEN":
            canvas = d.screen
            center = (d.width//2,d.height//2)

        else:
            center = canvas.get_rect().center

        if size != 1:
            surface = pygame.transform.smoothscale(surface,
                                   (d.zoom*size,
                                    d.zoom*size))
        else:
            surface = self.surface
        
        
        canvas.blit(surface,(center[0] - self.rect[0] + pos[0]*d.zoom,
                             center[1] - self.rect[1] - pos[1]*d.zoom))

    def resize(self, mainself):
        
        scene = mainself.Scene.Game

        self.surface = pygame.Surface((600 * self.size * mainself.Display.zoom,
                                       600 * self.size * mainself.Display.zoom),
                                       pygame.SRCALPHA)
        
        self.rect = self.surface.get_rect().center
        
        self.surface.set_alpha(self.transparency*255)
        
        line = mainself.Asset.Line(mainself, width = 3)
        
        line.draw(mainself,(0,100),self.surface)
        line.draw(mainself,(0,-100),self.surface)
        
        # вот тут доделать баля
        
        line.draw(mainself,(-100,0),self.surface)
        line.draw(mainself,(100,0),self.surface)