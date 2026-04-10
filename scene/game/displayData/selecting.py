import math

class Selecting:
    '''Класс для отображения выбыраемой клетки'''

    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса отображения выбора клетки сцены Game.","DEBUG")

        # переменная для "моргания" выделения
        self.time = 0

    def main(self, mainself):
        '''Рисует выбираемые клетки'''
        
        scene = mainself.Scene.Game

        # если клетка не выбранна, то выбираем большую клетку
        if scene.Logic.Game.selected_cell == None:
            self.selecting_big_cell(mainself)

        # выбираем маленькую клетку
        else:
            self.selecting_small_cell(mainself)

        # добавляем время к таймеру моргания
        self.time += 1/10 * mainself.Display.speed
        
        # обновляем таймер
        if self.time > math.pi * 2:
            self.time -= math.pi * 2
    
    def selecting_big_cell(self, mainself):
        '''Выбор большой клетки'''

        scene = mainself.Scene.Game

        # выбираемая клетка
        selecting_cell = scene.Logic.Select.select_big_cell(mainself)
        
        # если пользователь выбрал клетку и данная клетка пуста
        if selecting_cell != None and None in scene.Logic.Game.cells[selecting_cell]:
            
            # выбыраем спрайт в зависимости от игрока который выбирает клетку
            if scene.Logic.Game.player == 0:
                asset = scene.Selecting0
            else:
                asset = scene.SelectingX

            # рисуем спрайт
            asset.draw(mainself,(200*(selecting_cell%3-1),
                                -200*(selecting_cell//3-1)),
                                transparency = math.sin(self.time)/4+0.25)
            
        # если режим выделения - клавиатура, то нужно так же указать что клетку нельзя выбрать
        elif mainself.Event.mode == "KEYBOARD":
            
            # особый спрайт
            asset = scene.UnablSelecting

            # рисуем спрайт
            asset.draw(mainself,(200*(selecting_cell%3-1),
                                -200*(selecting_cell//3-1)))
    
    def selecting_small_cell(self, mainself):
        '''Выбор маленькой клетки'''

        scene = mainself.Scene.Game

        # выбираемая клетка
        selecting_cell = scene.Logic.Select.select_small_cell(mainself)

        # если пользователь выбрал клетку и данная клетка пуста
        if selecting_cell != None and scene.Logic.Game.cells[scene.Logic.Game.selected_cell][selecting_cell] == None:

            # выбыраем спрайт в зависимости от игрока который выбирает клетку
            if scene.Logic.Game.player == 0:
                asset = scene.SmallCircle
            else:
                asset = scene.SmallCross

            # рисуем спрайт
            asset.draw(mainself,(200*(scene.Logic.Game.selected_cell%3-1)+50*(selecting_cell%3-1),
                            -200*(scene.Logic.Game.selected_cell//3-1)-50*(selecting_cell//3-1)),
                            transparency = math.sin(self.time)/4+0.25)
        
        # если режим выделения - клавиатура, то нужно так же указать что клетку нельзя выбрать
        elif mainself.Event.mode == "KEYBOARD":

            # особый спрайт
            asset = scene.UnablSelecting

            # рисуем спрайт
            asset.draw(mainself,(200*(scene.Logic.Game.selected_cell%3-1)+50*(selecting_cell%3-1),
                            -200*(scene.Logic.Game.selected_cell//3-1)-50*(selecting_cell//3-1)), 0.20)