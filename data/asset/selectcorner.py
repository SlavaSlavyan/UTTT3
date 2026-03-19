import pygame
import math

class SelectCorner:

    def __init__(self, mainself, angle:int, base_size:float = 1):
        
        self.base_size = base_size
        self.angle = angle

        self.resize(mainself)

    def draw(self, mainself, pos:tuple, canvas:pygame.surface.Surface = "SCREEN"):

        display = mainself.Display

        if canvas == "SCREEN":
            canvas = display.screen
            center = (display.width//2,display.height//2)

        else:
            center = canvas.get_rect().center

        rect = list(self.rect)

        if math.sin(math.radians(self.angle)) >= 0:
            rect[0] = 0
        
        if math.cos(math.radians(self.angle)) >= 0:
            rect[1] = 0

        display.screen.blit(self.surface,(center[0] - rect[0] + pos[0]*display.zoom,
                             center[1] - rect[1] - pos[1]*display.zoom))

    def resize(self, mainself):

        self.surface = pygame.Surface((4, 4), pygame.SRCALPHA)

        pygame.draw.line(self.surface, mainself.Display.colors["game"]["select-corner"],(0,0),(0,3))
        pygame.draw.line(self.surface, mainself.Display.colors["game"]["select-corner"],(0,0),(3,0))

        self.surface = pygame.transform.scale(self.surface, (200 * self.base_size * mainself.Display.zoom,
                                                                   200 * self.base_size * mainself.Display.zoom))
        
        if self.angle != 0:
            self.surface = pygame.transform.rotate(self.surface, self.angle)

        self.rect = self.surface.get_rect().size