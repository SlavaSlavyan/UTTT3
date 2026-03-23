from scene.game.display import Display
from scene.game.logic import Logic

class Game:

    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация сцены Game.","DEBUG")

        self.status = 0
        
        mainself.Asset.load(mainself,"BgRect")
        mainself.Asset.load(mainself,"Line")
        mainself.Asset.load(mainself,"Cells")
        mainself.Asset.load(mainself,"Corner")
        mainself.Asset.load(mainself,"Select")
        mainself.Asset.load(mainself,"Circle")
        mainself.Asset.load(mainself,"Cross")
        
        self.Bg = mainself.Asset.BgRect(mainself)
        self.LineHorizontal = mainself.Asset.Line(mainself)
        self.LineVertical = mainself.Asset.Line(mainself,90)
        self.SmallCells = mainself.Asset.Cells(mainself, 0.25, 0.25, 3)
        self.corners = []

        for i in range(4):
            self.corners.append(mainself.Asset.Corner(mainself, 90*i))
        
        self.Display = Display(mainself)
        self.Logic = Logic(mainself)