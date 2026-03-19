import pygame

class Line:

    def __init__(self, mainself, angle:int = 0, width:int = 5):
        
        self.angle = angle
        self.width = width
        
        self.resize(mainself)

    def draw(self, mainself, pos:tuple, canvas:pygame.surface.Surface = "SCREEN"):

        display = mainself.Display

        if canvas == "SCREEN":
            canvas = display.screen
            center = (display.width//2,display.height//2)

        else:
            center = canvas.get_rect().center
        
        canvas.blit(self.surface,(center[0] - self.rect[0] + pos[0]*display.zoom,
                             center[1] - self.rect[1] - pos[1]*display.zoom))

    def resize(self, mainself):

        self.surface = pygame.Surface((600*mainself.Display.zoom,
                                       self.width*mainself.Display.zoom))
        
        self.surface.fill(mainself.Display.colors["game"]["line"])
        
        if self.angle != 0:
            self.surface = pygame.transform.rotate(self.surface,self.angle)
        
        self.rect = self.surface.get_rect().center