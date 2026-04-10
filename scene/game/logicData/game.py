class Game:
    '''Класс логики ИГРЫ'''
    
    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса логики игры сцены Game. (ну типо да, логика самой игры)","DEBUG")
        
        # большая выбранная клетка
        self.selected_cell = None

        # игрок который сейчас делает ход
        self.player = 0

        # статус победы
        self.win = None

        # Двухмерный массив со всеми клетками
        self.cells = []

        # Добавляем начальное значение в каждую клетку
        for i in range(9):
            self.cells.append([])

            for j in range(9):
                self.cells[i].append(None)
    
    def main(self, mainself):
        '''Ход любого из игроков'''
        
        mainself.Log.write("Запуск функции логики игры.")
        
        # если большая клетка не выбрана её нужно выбрать
        if self.selected_cell == None:
            # в функцию сразу встраивается выбранная клетка из класса Logic.Select
            self.check_big_selected_cell(mainself, mainself.Scene.Game.Logic.Select.select_big_cell(mainself))

        # выбор маленькой клетки
        else:
            # в функцию сразу встраивается выбранная клетка из класса Logic.Select
            self.check_small_selected_cell(mainself, mainself.Scene.Game.Logic.Select.select_small_cell(mainself))
    
    def check_big_selected_cell(self, mainself, cell:int):
        '''Выбор большой клетки.
        - **cell**: Клетка которую выбрал пользователь'''
        
        mainself.Log.write(f"Проверка выбранной большой клетки. Cell = {cell}")
        
        # проверяем выбрал ли пользователь клетку
        if cell != None:

            # проверяем есть ли пустые клетки в выбираемой клетке
            if None in self.cells[cell]:

                # перезаписываем выбранную клетку
                self.selected_cell = cell
                mainself.Log.write(f"Выбранна клетка {cell}")
                
                return
            
            else:
                
                # обнуляем значение
                self.selected_cell = None
                mainself.Log.write("Клетка занята.")
                
                return
        
        mainself.Log.write("Клетка не выбрана.")
    
    def check_small_selected_cell(self, mainself, cell:int):
        '''Выбор маленькой клетки.
        - **cell**: Клетка которую выбрал пользователь'''
        
        mainself.Log.write(f"Проверка выбранной маленькой клетки. Cell = {cell}")

        # проверяем выбрал ли пользователь клетку
        if cell != None:
            
            # проверяем пуста ли клетка
            if self.cells[self.selected_cell][cell] == None:
                
                # перезаписываем выбранную клетку
                self.cells[self.selected_cell][cell] = self.player
                mainself.Log.write(f"Данные клетки {self.selected_cell} были перезаписанны.\n{self.cells[self.selected_cell]}")

                # проверяем захваченна ли клетка
                result = self.check_capture(mainself)

                if result:

                    mainself.Log.write(f"Клетка захвачена.")

                    # заполняем всю большую клетку
                    for i in range(9): 
                        self.cells[self.selected_cell][i] = self.player

                    mainself.Log.write(f"Данные клетки {self.selected_cell} были перезаписанны.\n{self.cells[self.selected_cell]}")

                    # проверяем победу игрока
                    result = self.check_win(mainself)

                    if result:

                        mainself.Log.write(f"Игрок {self.player} победил!")
                        
                        # записываем победу
                        self.win = self.player
                        
                        # переходим на следующий статус
                        self.next_status(mainself)

                        # прерываем функцию
                        return
            
                # проверяем возможность ничьи
                result = self.check_draw(mainself)
                
                if result:
                    
                    mainself.Log.write(f"Ничья!")
                    
                    # записываем ничью
                    self.win = -1
                    
                    # переходим на следующий статус
                    self.next_status(mainself)

                    # прерываем функцию
                    return

                # следующий игрок
                if self.player:
                    self.player = 0
                else:
                    self.player = 1

                mainself.Log.write(f"Смена игрока ({self.player}).")
                
                # выбираем следующую клетку
                mainself.Log.write(f"Выбор следующей клетки.")
                self.check_big_selected_cell(mainself,cell)
                    
            else:
                mainself.Log.write("Клетка занята.")
                
        else:
            mainself.Log.write("Клетка не выбрана.")
    
    def check_capture(self, mainself) -> bool:
        '''Проверка захвата клетки.\n
        Вернёт булевое выражение в зависимости от результата'''
        
        mainself.Log.write(f"Проверка захвата клетки.")

        # берём проверяемую клетку
        cell = self.cells[self.selected_cell]
        
        # повторяем все действия по 3 раза со сдвигом
        for i in range(3):
            
            # проверка по горизонтали
            if cell[3*i] == self.player and cell[1+3*i] == self.player and cell[2+3*i] == self.player:
                return True
            
            # проверка по вертикали
            if cell[i] == self.player and cell[3+i] == self.player and cell[6+i] == self.player:
                return True
        
        # две проверки по диагонялям

        if cell[0] == self.player and cell[4] == self.player and cell[8] == self.player:
            return True
        
        if cell[2] == self.player and cell[4] == self.player and cell[6] == self.player:
            return True
        
        mainself.Log.write(f"Клетка не захвачена.")
        return False

    def check_win(self, mainself) -> bool:
        '''Проверка выйгрыша.\n
        Вернёт булевое выражение в зависимости от результата'''
        
        mainself.Log.write(f"Проверка выйгрыша.")

        # ассет захваченной клетки
        win = []

        # заполняем массив нынешним игроком
        for i in range(9):
            win.append(self.player)
        
        # повторяем все действия по 3 раза со сдвигом
        for i in range(3):
            
            # проверка по горизонтали
            if self.cells[3*i] == win and self.cells[1+3*i] == win and self.cells[2+3*i] == win:
                return True
            
            # проверка по вертикали
            if self.cells[i] == win and self.cells[3+i] == win and self.cells[6+i] == win:
                return True
        
        # две проверки по диагонялям

        if self.cells[0] == win and self.cells[4] == win and self.cells[8] == win:
            return True
        
        if self.cells[2] == win and self.cells[4] == win and self.cells[6] == win:
            return True
        
        mainself.Log.write(f"Никто не выйграл.")
        return False

    def check_draw(self, mainself) -> bool:
        '''Проверка ничьи.
        Вернёт булевое выражение в зависимости от результата'''
        
        mainself.Log.write(f"Проверка ничьи.")
        
        # ищем пустые клетки в больших клетках
        for i in range(9):
            if None in self.cells[i]:
                
                mainself.Log.write(f"Игра продолжается.")
                return False
        
        # иначе ходов больше сделать нельзя
        return True
    
    def next_status(self, mainself):
        '''Функция запускает переход на следующий статус и задаёт необходимые настройки'''
        
        mainself.Log.write("Новый статус сцены Game. (2)")

        # обнуляем значение выделенной клетки
        self.selected_cell = None

        # создаём табличку победы
        mainself.Scene.Game.Display.WinLabel.create_label(mainself,self.win)

        # ставим следующий статус
        mainself.Scene.Game.status = 2
        
        # перерисовываем спрайты
        mainself.Scene.Game.Display.on_resize(mainself)