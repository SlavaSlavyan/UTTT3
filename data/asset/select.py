import pygame

class Select:
    
    def __init__(self, mainself, base_size:float = 1, color:tuple = "DEFAULT"):
        
        mainself.Log.write(f"Создан экземпляр спрайта выбора клетки.\nБазовый размер = {base_size}\nЦвет = {color}","DEBUG")
        
        self.base_size = base_size
        self.color = color
        
        self.pos = [0,0]
        self.offset = [0,0]
        self.size = 1
        self.selected_cell = None
        
        self.resize(mainself)
    
    def draw(self, mainself, pos:int = "LOCAL", size:float = "DEFAULT", transparency:float = 1):
        
        display = mainself.Display
        
        if size == "DEFAULT":
            
            surface = self.surface
            size = self.base_size
            rect = self.rect

        else: 
            
            if size == "LOCAL":
                size = self.size
                
            surface = pygame.transform.smoothscale(self.surface,
                                   (750 * display.zoom * size * self.base_size,
                                    750 * display.zoom * size * self.base_size)),
            surface = surface[0]
            
            rect = surface.get_rect().center
        
        if transparency != 1:
            
            if surface == self.surface:
                surface = self.surface.copy()
            
            surface.set_alpha(transparency*255)
        
        if pos == "LOCAL":
            pos = (self.pos[0] + self.offset[0], self.pos[1] + self.offset[1])
        
        display.screen.blit(surface,
                      (display.width//2 - rect[0] + pos[0]*display.zoom,
                       display.height//2 - rect[1] - pos[1]*display.zoom))
        
        self.logic(mainself)
    
    def resize(self, mainself):
        
        mainself.Log.write(f"Перерисовка спрайта выбора клетки")
        
        self.surface = pygame.Surface((750 * mainself.Display.zoom,
                                       750 * mainself.Display.zoom),
                                       pygame.SRCALPHA)
        
        corners = []
        
        for i in range(4):
            corners.append(mainself.Asset.Corner(mainself, 90*i, color = self.color))

        corners[0].draw(mainself,(-375,375),(0,0), self.surface)
        corners[1].draw(mainself,(-375,-375),(0,1), self.surface)
        corners[2].draw(mainself,(375,-375),(1,1), self.surface)
        corners[3].draw(mainself,(375,375),(1,0), self.surface)
        
        self.surface = pygame.transform.scale(self.surface, (750 * self.base_size * mainself.Display.zoom,
                                                             750 * self.base_size * mainself.Display.zoom))
        
        self.rect = self.surface.get_rect().center

    def logic(self, mainself):
        
        if self.selected_cell != mainself.Scene.Game.Logic.Game.selected_cell:
            self.newpos(mainself)

        self.newsize(mainself)
        
        self.offset[0] /= 1 + 0.1 * mainself.Display.speed
        self.offset[1] /= 1 + 0.1 * mainself.Display.speed
    
    def newpos(self,mainself):
        
        self.selected_cell = mainself.Scene.Game.Logic.Game.selected_cell
        
        now = (self.pos[0] + self.offset[0], self.pos[1] + self.offset[1])
        
        if self.selected_cell == None: 
            x, y = 0, 0
        else:
            x = (self.selected_cell%3) - 1
            y = (self.selected_cell//3) - 1
        
        self.pos = [200*x,200*-y]
        self.offset = [now[0]-self.pos[0],now[1]-self.pos[1]]
        
    def newsize(self,mainself):
        
        if self.selected_cell == None:
            
            if self.size < 1:
                self.size += 1/30 * mainself.Display.speed
            
            if self.size > 1:
                self.size = 1
        
        else:
            
            if self.size > 0.25:
                self.size -= 1/30 * mainself.Display.speed
            
            if self.size < 0.25:
                self.size = 0.25