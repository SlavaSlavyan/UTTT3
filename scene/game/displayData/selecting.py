import math

class Selecting:

    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса отображения выбора клетки сцены Game.","DEBUG")

        self.time = 0

    def main(self, mainself):
        
        scene = mainself.Scene.Game

        if scene.Logic.Game.selected_cell == None:

            self.selecting_cell = scene.Logic.Select.select_big_cell(mainself)
            
            if self.selecting_cell != None and None in scene.Logic.Game.cells[self.selecting_cell]:
                
                if scene.Logic.Game.player == 0:
                    asset = scene.Selecting0
                else:
                    asset = scene.SelectingX

                asset.draw(mainself,(200*(self.selecting_cell%3-1),
                                    -200*(self.selecting_cell//3-1)),
                                    transparency = math.sin(self.time)/4+0.25)
                
            elif scene.Logic.Select.mode == "KEYBOARD":

                asset = scene.UnablSelecting

                asset.draw(mainself,(200*(self.selecting_cell%3-1),
                                    -200*(self.selecting_cell//3-1)))

        else:

            self.selecting_cell = scene.Logic.Select.select_small_cell(mainself)

            asset = None

            if self.selecting_cell != None and scene.Logic.Game.cells[scene.Logic.Game.selected_cell][self.selecting_cell] == None:

                if scene.Logic.Game.player == 0:
                    asset = scene.SmallCircle
                else:
                    asset = scene.SmallCross

                asset.draw(mainself,(200*(scene.Logic.Game.selected_cell%3-1)+50*(self.selecting_cell%3-1),
                                -200*(scene.Logic.Game.selected_cell//3-1)-50*(self.selecting_cell//3-1)),
                                transparency = math.sin(self.time)/4+0.25)
            
            elif scene.Logic.Select.mode == "KEYBOARD":

                asset = scene.UnablSelecting

                asset.draw(mainself,(200*(scene.Logic.Game.selected_cell%3-1)+50*(self.selecting_cell%3-1),
                                -200*(scene.Logic.Game.selected_cell//3-1)-50*(self.selecting_cell//3-1)),
                                0.20)

        self.time += 1/10 * mainself.Display.speed

        if self.time > math.pi * 2:
            self.time -= math.pi * 2