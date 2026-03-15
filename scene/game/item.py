from scene.game.itemData.bg_rect import BgRect
from scene.game.itemData.line import Line
from scene.game.itemData.cells import Cells

class Item:

    def __init__(self, mainself):
        
        self.BgRect = BgRect(mainself)
        self.Line = Line(mainself)
        self.Cells = Cells(mainself)