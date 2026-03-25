import pygame

class Cursor:
    
    def __init__(self, mainself):
        
        mainself.Log.write(f"Создан экземпляр спрайта курсора.","DEBUG")
        
        self.transparency = 1
        
        self.resize(mainself)
    
    def draw(self, mainself):
        
        if self.transparency != 1:
            
            surface = self.surface.copy()
            surface.set_alpha(self.transparency*255)
        
        else:
            surface = self.surface
        
        if self.transparency != 0:
            mainself.Display.screen.blit(surface, mainself.Event.Mouse.pos)
        
        self.logic(mainself)
    
    def resize(self, mainself):
        
        mainself.Log.write(f"Перерисовка спрайта курсора")
        
        self.surface = pygame.Surface((10,10),pygame.SRCALPHA)
        
        points = [(0,0),(9,0),(0,9)]
        
        pygame.draw.polygon(self.surface,mainself.Display.colors["global"]["cursor"],points)
    
    def logic(self, mainself):
        
        if mainself.Event.mode == "MOUSE":
            
            if self.transparency < 1:
                self.transparency += 1/15 * mainself.Display.speed
            
            if self.transparency > 1:
                self.transparency = 1
        
        else:
            
            if self.transparency > 0:
                self.transparency -= 1/15 * mainself.Display.speed
            
            if self.transparency < 0:
                self.transparency = 0