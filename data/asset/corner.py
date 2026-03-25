import pygame

class Corner:

    def __init__(self, mainself, angle:int, base_size:float = 1, color:tuple = "DEFAULT"):
        
        mainself.Log.write(f"Создан экземпляр спрайта уголка выделения клетки.\nПоворот = {angle}\nНачальный размер = {base_size}\nЦвет = {color}","DEBUG")
        
        self.base_size = base_size
        self.angle = angle
        
        if color == "DEFAULT":
            self.color = mainself.Display.colors["game"]["select-corner"]
        else:
            self.color = color

        self.resize(mainself)

    def draw(self, mainself, pos:tuple, rect_align:tuple, canvas:pygame.surface.Surface = "SCREEN"):

        display = mainself.Display

        if canvas == "SCREEN":
            canvas = display.screen
            center = (display.width//2,display.height//2)

        else:
            center = canvas.get_rect().center

        rect = (self.rect[0]*rect_align[0],self.rect[1]*rect_align[1])

        canvas.blit(self.surface,(center[0] - rect[0] + pos[0]*display.zoom,
                             center[1] - rect[1] - pos[1]*display.zoom))

    def resize(self, mainself):
        
        mainself.Log.write(f"Перерисовка спрайта уголка выделения клетки.")

        self.surface = pygame.Surface((4, 4), pygame.SRCALPHA)

        pygame.draw.line(self.surface, self.color,(0,0),(0,3))
        pygame.draw.line(self.surface, self.color,(0,0),(3,0))

        self.surface = pygame.transform.scale(self.surface, (200 * self.base_size * mainself.Display.zoom,
                                                             200 * self.base_size * mainself.Display.zoom))
        
        if self.angle != 0:
            self.surface = pygame.transform.rotate(self.surface, self.angle)

        self.rect = self.surface.get_rect().size