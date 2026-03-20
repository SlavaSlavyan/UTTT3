import pygame

from scene.game.logicData.select import Select
from scene.game.logicData.game import Game

class Logic:

    def __init__(self, mainself):
        
        self.Select = Select(mainself)
        self.Game = Game(mainself)
        
    def main(self, mainself):

        if mainself.Scene.Game.status == 1:
            
            if mainself.Event.Mouse.keys['lt']['press']:
                
                self.Game.main(mainself)