import pygame

class BgRect:

    def __init__(self, mainself):
        pass

    def draw(self, mainself, size:float = 1):

        d = mainself.Display

        if size == 1:
            surface = self.surface

        else:
            surface = pygame.transform.scale(self.surface,
                                   (600*d.zoom*size,
                                    600*d.zoom*size)),
            surface = surface[0]
        
        d.screen.blit(surface,
                      (d.width//2 - surface.get_rect().centerx,
                       d.height//2 - surface.get_rect().centery))

    def resize(self, mainself):
        
        self.surface = pygame.Surface((600*mainself.Display.zoom,
                                       600*mainself.Display.zoom))
        self.surface.fill(mainself.Scene.Game.Display.colors["rect-bg"])