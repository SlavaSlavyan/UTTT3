STARTING_POINT = 4 # начальная позиция для режима клавиатуры

class Select:
    '''Класс обработки отслеживания взаисодействия с клетками'''
    
    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса выбора клеток в сцене Game.","DEBUG")

        # клетка на которую сделан акцент
        # нужна для выбора клетки в режиме клавиатуры
        self.selecting = STARTING_POINT
    
    def select_big_cell(self, mainself) -> int | None:
        '''Выбирает большую клетку\n
        Возвращает ничего если в режими мыши в клетку не попали'''

        # режим мыши
        if mainself.Event.mode == "MOUSE":

            # конвертируем координаты в x и y
            x = (mainself.Event.Mouse.pos[0] - mainself.Display.width//2) / mainself.Display.zoom
            y = (mainself.Event.Mouse.pos[1] - mainself.Display.height//2) / -mainself.Display.zoom
            
            # проверяем попадание в доступные клетки
            for Y in range(3):
                for X in range(3):
                    
                    if y < 300-200*Y and y > 100-200*Y and x > -300+200*X and x < -100+200*X:
                        return X + 3*Y
            
            # возращаем ничего если в клетку не попали
            return None

        # режим клавиатуры. Вызывается отдельная функция для выбора клетки
        else: 
            return self.select_keyboard(mainself)
    
    def select_small_cell(self, mainself):
        '''Выбирает маленькую клетку\n
        Возвращает ничего если в режими мыши в клетку не попали'''

        # режим мыши
        if mainself.Event.mode == "MOUSE":

            # конвертируем координаты в x и y с учётом выбранной большой клетки в классе Logic.Game
            x = (mainself.Event.Mouse.pos[0] - mainself.Display.width//2 - 200*(mainself.Scene.Game.Logic.Game.selected_cell%3-1)*mainself.Display.zoom) / mainself.Display.zoom
            y = (mainself.Event.Mouse.pos[1] - mainself.Display.height//2 - 200*(mainself.Scene.Game.Logic.Game.selected_cell//3-1)*mainself.Display.zoom) / -mainself.Display.zoom
            
            # проверяем попадание в доступные клетки
            for Y in range(3):
                for X in range(3):
                    
                    if y < 75-50*Y and y > 25-50*Y and x > -75+50*X and x < -25+50*X:
                        return X + 3*Y

            # возращаем ничего если в клетку не попали    
            return None
        
        # режим клавиатуры. Вызывается отдельная функция для выбора клетки
        else: 
            return self.select_keyboard(mainself)
    
    def select_keyboard(self, mainself) -> int:
        '''Выбор клетки во время режима клавиатуры\n
        Обычно вызывается внутри функций выбора клеток'''

        # получаем список клавиш
        keys = mainself.Event.KeyBoard.keys

        # изменяем положение выбранной клетки
        if keys["up"]["press"] and self.selecting//3 > 0:
            self.selecting -= 3
        if keys["down"]["press"] and self.selecting//3 < 2:
            self.selecting += 3
        if keys["left"]["press"] and self.selecting%3 > 0:
            self.selecting -= 1
        if keys["right"]["press"] and self.selecting%3 < 2:
            self.selecting += 1

        # возвращаем выбранную клетку
        return self.selecting
    
    def update_mode(self, mainself) -> bool:
        '''Обновление режима выбора клеток\n
        Если состояние было обновленно - вернёт **True**'''

        if mainself.Event.mode == "MOUSE":

            # получаем список клавиш
            keys = mainself.Event.KeyBoard.keys

            # если была нажата клавиша перемещения выбора клетки или сам выбор клетки, то меняем режим
            if keys["input"]["press"] or keys["down"]["press"] or keys["up"]["press"] or keys["left"]["press"] or keys["right"]["press"]:

                mainself.Event.mode = "KEYBOARD"
                self.selecting = STARTING_POINT

                return True
        
        else:
            
            # получаем кнопки мыши
            keys = mainself.Event.Mouse.keys

            # если была нажата любая кнопка, то меняем режим
            if keys["lt"]["press"] or keys["md"]["press"] or keys["rt"]["press"]:

                mainself.Event.mode = "MOUSE"
                self.selecting = STARTING_POINT

                return True
        
        return False