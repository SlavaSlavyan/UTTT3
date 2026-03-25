class Select:
    
    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса выбора клеток в сцене Game.","DEBUG")

        self.selecting = None
    
    def select_big_cell(self, mainself):

        if mainself.Event.mode == "MOUSE":
        
            x = (mainself.Event.Mouse.pos[0] - mainself.Display.width//2) / mainself.Display.zoom
            y = (mainself.Event.Mouse.pos[1] - mainself.Display.height//2) / -mainself.Display.zoom
            
            for Y in range(3):
                for X in range(3):
                    
                    if y < 300-200*Y and y > 100-200*Y and x > -300+200*X and x < -100+200*X:
                        return X + 3*Y
                        
            return None

        else:

            return self.select_keyboard(mainself)
    
    def select_small_cell(self, mainself):

        if mainself.Event.mode == "MOUSE":

            x = (mainself.Event.Mouse.pos[0] - mainself.Display.width//2 - 200*(mainself.Scene.Game.Logic.Game.selected_cell%3-1)*mainself.Display.zoom) / mainself.Display.zoom
            y = (mainself.Event.Mouse.pos[1] - mainself.Display.height//2 - 200*(mainself.Scene.Game.Logic.Game.selected_cell//3-1)*mainself.Display.zoom) / -mainself.Display.zoom
            
            for Y in range(3):
                for X in range(3):
                    
                    if y < 75-50*Y and y > 25-50*Y and x > -75+50*X and x < -25+50*X:
                        return X + 3*Y
                        
            return None
        
        else:
            
            return self.select_keyboard(mainself)
    
    def select_keyboard(self, mainself):

        keys = mainself.Event.KeyBoard.keys
            
        if self.selecting != None:

            if keys["up"]["press"] and self.selecting//3 > 0:
                self.selecting -= 3
            if keys["down"]["press"] and self.selecting//3 < 2:
                self.selecting += 3
            if keys["left"]["press"] and self.selecting%3 > 0:
                self.selecting -= 1
            if keys["right"]["press"] and self.selecting%3 < 2:
                self.selecting += 1

        return self.selecting
    
    def update_mode(self, mainself):

        if mainself.Event.mode == "MOUSE":

            keys = mainself.Event.KeyBoard.keys

            if keys["input"]["press"] or keys["down"]["press"] or keys["up"]["press"] or keys["left"]["press"] or keys["right"]["press"]:

                mainself.Event.mode = "KEYBOARD"
                self.selecting = 4

                return True
        
        else:

            keys = mainself.Event.Mouse.keys

            if keys["lt"]["press"] or keys["md"]["press"] or keys["rt"]["press"]:

                mainself.Event.mode = "MOUSE"
                self.selecting = None

                return True
        
        return False