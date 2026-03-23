import pygame

class Select:
    
    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса выбора клеток в сцене Game.","DEBUG")
    
    def select_big_cell(self, mainself):
        
        x = (mainself.Event.Mouse.pos[0] - mainself.Display.width//2) / mainself.Display.zoom
        y = (mainself.Event.Mouse.pos[1] - mainself.Display.height//2) / -mainself.Display.zoom
        
        for Y in range(3):
            for X in range(3):
                
                if y < 300-200*Y and y > 100-200*Y and x > -300+200*X and x < -100+200*X:
                    return X + 3*Y
                    
        return None
    
    def select_small_cell(self, mainself):

        x = (mainself.Event.Mouse.pos[0] - mainself.Display.width//2 - 200*(mainself.Scene.Game.Logic.Game.selected_cell%3-1)*mainself.Display.zoom) / mainself.Display.zoom
        y = (mainself.Event.Mouse.pos[1] - mainself.Display.height//2 - 200*(mainself.Scene.Game.Logic.Game.selected_cell//3-1)*mainself.Display.zoom) / -mainself.Display.zoom
        
        for Y in range(3):
            for X in range(3):
                
                if y < 75-50*Y and y > 25-50*Y and x > -75+50*X and x < -25+50*X:
                    return X + 3*Y
                    
        return None