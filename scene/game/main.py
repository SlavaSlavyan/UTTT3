from scene.game.display import Display
from scene.game.logic import Logic

# статическое значение прозрачности клетки в котором она находится большую часть времени
from scene.game.displayData.cells import STATIC_TRANSPARENCY_VALUE as STV_CELLS

ADDITIONAL_SELECTING_SIZE = 0.25 # размер дополнительных выделение клеток
SMALL_FIGURES_SIZES = 0.20       # размер маленьких фигур
BIG_FIGURES_SIZES = 0.75         # размер больших фигур

class Game:
    '''Класс сцены игры'''

    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация сцены Game.","DEBUG")

        # локальный статус сцены
        self.status = 0
        
        # загрузка необходимых ассетов
        mainself.Asset.load(mainself,"BgRect")
        mainself.Asset.load(mainself,"Line")
        mainself.Asset.load(mainself,"Cells")
        mainself.Asset.load(mainself,"Corner")
        mainself.Asset.load(mainself,"Select")
        mainself.Asset.load(mainself,"Circle")
        mainself.Asset.load(mainself,"Cross")
        mainself.Asset.load(mainself,"Label")
        
        # создаём необходимые экземпляры ассетов
        self.Bg = mainself.Asset.BgRect(mainself)
        self.LineHorizontal = mainself.Asset.Line(mainself)
        self.LineVertical = mainself.Asset.Line(mainself,90)
        self.SmallCells = mainself.Asset.Cells(mainself, STV_CELLS, 0.25, 3)
        self.Select = mainself.Asset.Select(mainself)
        self.Selecting0 = mainself.Asset.Select(mainself,ADDITIONAL_SELECTING_SIZE,mainself.Display.colors["game"]["circle"])
        self.SelectingX = mainself.Asset.Select(mainself,ADDITIONAL_SELECTING_SIZE,mainself.Display.colors["game"]["cross"])
        self.UnablSelecting = mainself.Asset.Select(mainself,ADDITIONAL_SELECTING_SIZE,mainself.Display.colors["game"]["unavailable"])
        self.SmallCircle = mainself.Asset.Circle(mainself,SMALL_FIGURES_SIZES)
        self.SmallCross = mainself.Asset.Cross(mainself,SMALL_FIGURES_SIZES)
        self.BigCircle = mainself.Asset.Circle(mainself,BIG_FIGURES_SIZES)
        self.BigCross = mainself.Asset.Cross(mainself,BIG_FIGURES_SIZES)

        self.corners = [] # уголков нам нужно 4, так что все ассеты храняться в массиве

        for i in range(4): 
            self.corners.append(mainself.Asset.Corner(mainself, 90*i))
        
        # отрисовка и логика
        self.Display = Display(mainself)
        self.Logic = Logic(mainself)