from scene.game.display import Display
from scene.game.logic import Logic

class Game:

    def __init__(self, mainself):

        self.status = 0
        
        mainself.Asset.load(mainself,"BgRect")
        mainself.Asset.load(mainself,"Line")
        
        self.Bg = mainself.Asset.BgRect(mainself)
        self.LineHorizontal = mainself.Asset.Line(mainself)
        self.LineVertical = mainself.Asset.Line(mainself,90)
        
        self.Display = Display(mainself)
        self.Logic = Logic(mainself)