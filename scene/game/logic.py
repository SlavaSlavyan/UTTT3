import pygame

from scene.game.logicData.select import Select
from scene.game.logicData.game import Game

class Logic:

    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса логики сцены Game.","DEBUG")
        
        self.Select = Select(mainself)
        self.Game = Game(mainself)
        
    def main(self, mainself):

        if mainself.Scene.Game.status == 1:

            update = self.Select.update_mode(mainself)
            
            if (mainself.Event.Mouse.keys['lt']['press'] or mainself.Event.KeyBoard.keys['input']['press']) and not update:
                
                self.Game.main(mainself)

                if mainself.Event.KeyBoard.keys['input']['press']:
                    self.Select.selecting = 4
        
        