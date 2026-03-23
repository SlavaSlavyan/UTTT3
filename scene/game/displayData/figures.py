class Figures:

    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса отображения фигур сцены Game.","DEBUG")
        
        self.small_figure_sizes = []

        for i in range(9):
            self.small_figure_sizes.append([])

            for j in range(9):
                self.small_figure_sizes[i].append(0)

    def main(self, mainself):
        
        for i in range(9):
            for j in range(9):

                self.draw_small_figures(mainself,i,j)

                self.new_small_figure_size(mainself,i,j)
    
    def new_small_figure_size(self,mainself,i,j):

        scene = mainself.Scene.Game
        cells = scene.Logic.Game.cells
        display = mainself.Display

        if cells[i][j] == 0:
                    
            if self.small_figure_sizes[i][j] < 1:
                self.small_figure_sizes[i][j] += 1/30 * display.speed
                if self.small_figure_sizes[i][j] > 1:
                    self.small_figure_sizes[i][j] = 1
        
        elif cells[i][j] == 1:

            if self.small_figure_sizes[i][j] > -1:
                self.small_figure_sizes[i][j] -= 1/30 * display.speed
                if self.small_figure_sizes[i][j] < -1:
                    self.small_figure_sizes[i][j] = -1
        
        else:

            if self.small_figure_sizes[i][j] < 0:
                self.small_figure_sizes[i][j] += 1/30 * display.speed
                if self.small_figure_sizes[i][j] > 0:
                    self.small_figure_sizes[i][j] = 0

            if self.small_figure_sizes[i][j] > 0:
                self.small_figure_sizes[i][j] -= 1/30 * display.speed
                if self.small_figure_sizes[i][j] < 0:
                    self.small_figure_sizes[i][j] = 0
    
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