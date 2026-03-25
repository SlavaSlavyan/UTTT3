class Figures:

    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса отображения фигур сцены Game.","DEBUG")
        
        self.small_figure_sizes = []
        self.big_figure_sizes = []

        for i in range(9):
            self.small_figure_sizes.append([])

            for j in range(9):
                self.small_figure_sizes[i].append(0)
                self.big_figure_sizes.append(0)

    def main(self, mainself):
        
        for i in range(9):

            for j in range(9):

                self.draw_small_figures(mainself,i,j)
                
                self.new_small_figure_size(mainself,i,j)

            self.draw_big_figures(mainself, i)
            
            self.new_big_figure_size(mainself, i)
    
    def new_small_figure_size(self,mainself,i,j):

        scene = mainself.Scene.Game
        cells = scene.Logic.Game.cells
        display = mainself.Display
        size = self.small_figure_sizes

        if None in cells[i] or len(set(cells[i])) != 1:

            if cells[i][j] == 0:
                        
                if size[i][j] < 1:
                    size[i][j] += 1/30 * display.speed
                    if size[i][j] > 1:
                        size[i][j] = 1
                
                return None
            
            if cells[i][j] == 1:

                if size[i][j] > -1:
                    size[i][j] -= 1/30 * display.speed
                    if size[i][j] < -1:
                        size[i][j] = -1
            
                return None

        if size[i][j] < 0:
            size[i][j] += 1/30 * display.speed
            if size[i][j] > 0:
                size[i][j] = 0

        if size[i][j] > 0:
            size[i][j] -= 1/30 * display.speed
            if size[i][j] < 0:
                size[i][j] = 0
    
    def draw_small_figures(self,mainself,i,j):

        scene = mainself.Scene.Game

        if self.small_figure_sizes[i][j] > 0:
            scene.SmallCircle.draw(mainself,(200*(i%3-1)+50*(j%3-1),
                                            -200*(i//3-1)-50*(j//3-1)),
                                            self.small_figure_sizes[i][j])
        
        if self.small_figure_sizes[i][j] < 0:
            scene.SmallCross.draw(mainself,(200*(i%3-1)+50*(j%3-1),
                                           -200*(i//3-1)-50*(j//3-1)),
                                           -self.small_figure_sizes[i][j])
    
    def new_big_figure_size(self,mainself,i):

        scene = mainself.Scene.Game
        cells = scene.Logic.Game.cells
        display = mainself.Display
        size = self.big_figure_sizes

        if all(x == 0 for x in cells[i]):
                    
            if size[i] < 1:
                size[i] += 1/45 * display.speed
                if size[i] > 1:
                    size[i] = 1
        
        elif all(x == 1 for x in cells[i]):

            if size[i] > -1:
                size[i] -= 1/45 * display.speed
                if size[i] < -1:
                    size[i] = -1
        
        else:

            if size[i] < 0:
                size[i] += 1/45 * display.speed
                if size[i] > 0:
                    size[i] = 0

            if size[i] > 0:
                size[i] -= 1/45 * display.speed
                if size[i] < 0:
                    size[i] = 0
    
    def draw_big_figures(self,mainself,i):

        scene = mainself.Scene.Game

        if self.big_figure_sizes[i] > 0:
            scene.BigCircle.draw(mainself,(200*(i%3-1),
                                            -200*(i//3-1)),
                                            self.big_figure_sizes[i])
        
        if self.big_figure_sizes[i] < 0:
            scene.BigCross.draw(mainself,(200*(i%3-1),
                                           -200*(i//3-1)),
                                           -self.big_figure_sizes[i])