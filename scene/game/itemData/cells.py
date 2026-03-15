import pygame

class Cells:

    def __init__(self, mainself):
        pass

    def draw(self, mainself, pos:tuple, transparency:float = 1, size:int = 1, type:str = "BIG", canvas:pygame.surface.Surface = "SCREEN"):

        d = mainself.Display

        if canvas == "SCREEN":
            canvas = d.screen
            center = (d.width//2,d.height//2)

        else:
            center = canvas.get_rect().center

        if type == "BIG":
            surface = self.surface
            base_size = 600
        else:
            surface = self.small_surface
            base_size = 150

        if size != 1:
            surface = pygame.transform.smoothscale(surface,
                                   (base_size*d.zoom*size,
                                    base_size*d.zoom*size))

        if transparency != 1:
            surface.set_alpha(transparency*255)
        
        rect = surface.get_rect().center
        
        canvas.blit(surface,(center[0] - rect[0] + pos[0]*d.zoom,
                             center[1] - rect[1] - pos[1]*d.zoom))

    def resize(self, mainself):

        line = mainself.Scene.Game.Item.Line

        self.surface = pygame.Surface((600*mainself.Display.zoom,
                                       600*mainself.Display.zoom),
                                       pygame.SRCALPHA)

        self.small_surface = pygame.Surface((200*mainself.Display.zoom,
                                       200*mainself.Display.zoom),
                                       pygame.SRCALPHA)
        
        line.draw(mainself,(0,-100),0,self.surface)
        line.draw(mainself,(0,100),0,self.surface)
        line.draw(mainself,(-100,0),90,self.surface)
        line.draw(mainself,(100,0),90,self.surface)

        line.draw(mainself,(0,-100/3),0,self.small_surface)
        line.draw(mainself,(0,100/3),0,self.small_surface)
        line.draw(mainself,(-100/3,0),90,self.small_surface)
        line.draw(mainself,(100/3,0),90,self.small_surface)

        self.small_surface = pygame.transform.smoothscale(self.small_surface,
                                   (150*mainself.Display.zoom,
                                    150*mainself.Display.zoom))