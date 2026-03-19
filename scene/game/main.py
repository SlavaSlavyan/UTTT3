from scene.game.display import Display
from scene.game.logic import Logic

class Game:

    def __init__(self, mainself):

        self.status = 0
        
        mainself.Asset.load(mainself,"BgRect")
        mainself.Asset.load(mainself,"Line")
        mainself.Asset.load(mainself,"Cells")
        mainself.Asset.load(mainself,"SelectCorner")
        
        self.Bg = mainself.Asset.BgRect(mainself)
        self.LineHorizontal = mainself.Asset.Line(mainself)
        self.LineVertical = mainself.Asset.Line(mainself,90)
        self.SmallCells = mainself.Asset.Cells(mainself, 0.25, 0.25, 3)
        self.corner = []

        for i in range(4):
            self.corner.append(mainself.Asset.SelectCorner(mainself, 90*i))
        
        self.Display = Display(mainself)
        self.Logic = Logic(mainself)