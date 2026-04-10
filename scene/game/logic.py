from scene.game.logicData.select import Select
from scene.game.logicData.game import Game

# начальная позиция для режима клавиатуры
from scene.game.logicData.select import STARTING_POINT

class Logic:
    '''Класс логики сцены игры'''

    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса логики сцены Game.","DEBUG")
        
        # логика выбора клеток
        self.Select = Select(mainself)
        
        # логика игры
        self.Game = Game(mainself)
        
    def main(self, mainself):
        '''Основная логика сцены игры'''

        # для проверки статуса берётся ЛОКАЛЬНЫЙ СТАТУС СЦЕНЫ!

        if mainself.Scene.Game.status == 1:
            
            # проверяем была ли смена управления с мыши на клавиатуру (или наоборот)
            update = self.Select.update_mode(mainself)
            
            # если кнопка\клавиша выбора была зажата и смены режима управления выбора не было, запускаем логику самой игры
            if (mainself.Event.Mouse.keys['lt']['press'] or mainself.Event.KeyBoard.keys['input']['press']) and not update:
                
                self.Game.main(mainself) # функция логики игры (ход)

                # обновляем позицию выбранной клетки для режима клавиатуры
                if mainself.Event.KeyBoard.keys['input']['press']:
                    self.Select.selecting = STARTING_POINT