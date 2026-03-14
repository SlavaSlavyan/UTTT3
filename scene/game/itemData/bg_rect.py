import pygame

class BgRect:

    def __init__(self, mainself):
        pass

    def draw(self, mainself):

        d = mainself.Display

        d.screen.blit(self.surface,(d.width//2 - self.surface.get_rect().centerx,
                                    d.height//2 - self.surface.get_rect().centery))

    def resize(self, mainself, size:float = 1):
        
        self.surface = pygame.Surface((600*mainself.Display.zoom*size,
                                       600*mainself.Display.zoom*size))
        self.surface.fill(mainself.Scene.Game.Display.colors["rect-bg"])