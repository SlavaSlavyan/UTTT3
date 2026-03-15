import pygame

class Line:

    def __init__(self, mainself):
        pass

    def draw(self, mainself, pos:tuple, angle:int = 0, canvas:pygame.surface.Surface = "SCREEN"):

        d = mainself.Display

        if canvas == "SCREEN":
            canvas = d.screen
            center = (d.width//2,d.height//2)

        else:
            center = canvas.get_rect().center

        if angle == 0:
            surface = self.surface
    
        else:
            surface = pygame.transform.rotate(self.surface,angle)
        
        rect = surface.get_rect().center
        
        canvas.blit(surface,(center[0] - rect[0] + pos[0]*d.zoom,
                             center[1] - rect[1] - pos[1]*d.zoom))

    def resize(self, mainself):

        self.surface = pygame.Surface((600*mainself.Display.zoom,
                                       5*mainself.Display.zoom))
        self.surface.fill(mainself.Scene.Game.Display.colors["line"])