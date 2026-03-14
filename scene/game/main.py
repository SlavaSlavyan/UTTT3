from scene.game.display import Display
from scene.game.logic import Logic
from scene.game.item import Item

class Game:

    def __init__(self, mainself):

        self.status = 0
        
        self.Item = Item(mainself)
        self.Display = Display(mainself)
        self.Logic = Logic(mainself)