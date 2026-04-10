MIN_SCREEN_SIZE = 300
MIN_FPS_VALUE = 10

class CheckFile:
    '''Класс проверки файлов программы'''
    
    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса проверки файлов программы.","DEBUG")
        
        # константы ПРАВИЛЬНЫХ файлов для восстановления
        
        # конфиг
        self.base_config = {
            "screen-size":[800,800], # начальный размер экрана
            "fullscreen":False,      # режим полного окна
            "max-fps":-1,            # максимальный FPS (-1 означает отсутствие ограничения)
            "debug":True             # режим отладки
        }
        
        # бинд клавиш
        self.base_bind = {
            "input":13,              # ввод информации
            "up":1073741906,         # перемещение вверх
            "down":1073741905,       # перемещение вниз
            "left":1073741904,       # перемещение влево
            "right":1073741903,      # перемещение вправо
            "fullscreen":1073741892, # переключение режима экрана
            "debug":1073741884       # переключение режима отладки
        }

        # палитра
        self.base_pallete = {
            "global":{ # цвета не привязанные к сцене
                "version-text":[171, 178, 191],
                "debug-text":[255,255,255],
                "cursor":[255,255,255]
            },
            "game":{ # сцена игры
                "bg":[40, 44, 52],
                "rect-bg":[33, 37, 43],
                "line":[171, 178, 191],
                "select-corner":[229, 192, 123],
                "circle":[97, 175, 239],
                "cross":[209, 154, 102],
                "unavailable":[224, 108, 117]
            }
        }
    
    def config(self, mainself, raw_config:any) -> dict:
        '''Возвращает корректный файл конфигурации
        - **raw_config**: изначальный не проверенный конфиг'''
        
        mainself.Log.write("Проверка конфигурации...")
        
        # главное исключение - проверка типа данных самого config
        if not isinstance(raw_config,dict):
            mainself.Log.write(f"Полученные данные не коректны! Будет загружет базовая конфигурация:\n{self.base_config}","ERROR")
            return self.base_config
        
        # добавление необходимых имён если они отсутствуют
        for i in self.base_config:

            if i not in raw_config:
                mainself.Log.write(f"Отсутствует имя {i}!","ERROR")
                raw_config[i] = self.base_config[i]
                
        # проверка отдельных полей
        
        # НАЧАЛЬНЫЙ РАЗМЕР ЭКРАНА
        if not isinstance(raw_config["screen-size"], list):
            mainself.Log.write(f"Неверный тип данных screen-size!","ERROR")
            raw_config["screen-size"] = self.base_config["screen-size"]
            
        for i in range(2):
            
            if not isinstance(raw_config["screen-size"][i], int):
                raw_config["screen-size"][i] = self.base_config["screen-size"][i]
                mainself.Log.write(f"Неверный тип данных внутри screen-size!","ERROR")
            
            if raw_config["screen-size"][i] < MIN_SCREEN_SIZE:
                mainself.Log.write(f"Неверный размер данных внутри screen-size!","ERROR")
                raw_config["screen-size"][i] = self.base_config["screen-size"][i]
                
        # ПОЛНЫЙ ЭКРАН
        if not isinstance(raw_config["fullscreen"], bool):
            mainself.Log.write(f"Неверный тип данных fullscreen!","ERROR")
            raw_config["fullscreen"] = self.base_config["fullscreen"]
        
        # МАКСИМАЛЬНЫЙ ФПС
        if not isinstance(raw_config["max-fps"], int):
            mainself.Log.write(f"Неверный тип данных max-fps!","ERROR")
            raw_config["max-fps"] = self.base_config["max-fps"]
        
        if raw_config["max-fps"] < MIN_FPS_VALUE and raw_config["max-fps"] != -1:
            mainself.Log.write(f"Неверный размер данных max-fps!","ERROR")
            raw_config["max-fps"] = self.base_config["max-fps"]
            
        # ОТЛАДКА
        if not isinstance(raw_config["debug"], bool):
            mainself.Log.write(f"Неверный тип данных debug!","ERROR")
            raw_config["debug"] = self.base_config["debug"]
        
        mainself.Log.write(f"Итоговая конфигурация:\n{raw_config}")
            
        return raw_config

    def bind(self, mainself, raw_bind:any) -> dict:
        '''Возвращает корректный файл биндинга клавиш
        - **raw_bind**: изначальный не проверенный бинд'''
        
        mainself.Log.write("Проверка биндов клавиш...")
        
        # главное исключение - проверка типа данных самого bind
        if not isinstance(raw_bind,dict):
            mainself.Log.write(f"Полученные данные не коректны! Будет загружет базовый бинд клавиш!:\n{self.base_bind}","ERROR")
            return self.base_bind
        
        # добавление необходимых имён если они отсутствуют
        for i in self.base_bind:

            if i not in raw_bind:
                mainself.Log.write(f"Отсутствует имя {i}!","ERROR")
                raw_bind[i] = self.base_bind[i]
        
        # цикл по всем биндам клавиш
        for i in raw_bind:
            
            # проверка типа данных
            if not isinstance(raw_bind[i], int):
                mainself.Log.write(f"Неверный тип данных {i}!","ERROR")
                raw_bind[i] = self.base_bind[i]
                
        mainself.Log.write(f"Итоговый бинд клавиш:\n{raw_bind}")
        
        return raw_bind

    def pallete(self, mainself, raw_pallete:any) -> dict:
        '''Возвращает корректный файл палитры
        - **raw_pallete**: изначальная не проверенная палитра'''
        
        mainself.Log.write("Проверка палитры...")
        
        # главное исключение - проверка типа данных самого pallete
        if not isinstance(raw_pallete,dict):
            mainself.Log.write(f"Полученные данные не коректны! Будет загружена базовая палитра!:\n{self.base_pallete}","ERROR")
            return self.base_pallete
        
        # цикл по всем коллекторам
        for i in self.base_pallete:

            # проверка 
            if i not in raw_pallete:
                mainself.Log.write(f"Отсутствует массив цветов {i}!","ERROR")
                raw_pallete[i] = self.base_pallete[i]
                continue

            # проверка типа данных
            if not isinstance(raw_pallete[i], dict):
                mainself.Log.write(f"Неверный тип данных {i}!","ERROR")
                raw_pallete[i] = self.base_pallete[i]
                continue
            
            # цикл по всем цветам
            for j in self.base_pallete[i]:

                # добавление необходимых имён если они отсутствуют
                if j not in raw_pallete[i]:
                    mainself.Log.write(f"Отсутствует имя {j} внутри {i}!","ERROR")
                    raw_pallete[i][j] = self.base_pallete[i][j]
                    continue

                # проверка типа данных
                if not isinstance(raw_pallete[i][j], list):
                    mainself.Log.write(f"Неверный тип данных {j} внутри {i}!","ERROR")
                    raw_pallete[i][j] = self.base_pallete[i][j]
                    continue
                
                # проверка длинны
                if len(raw_pallete[i][j]) != 3:
                    mainself.Log.write(f"Неверный размер данных {j} внутри {i}!","ERROR")
                    raw_pallete[i][j] = self.base_pallete[i][j]
                    continue

                # цикл по каждому элементу RGB
                for k in range(3):

                    # проверка типа данных
                    if not isinstance(raw_pallete[i][j][k], int):
                        mainself.Log.write(f"Неверный тип данных элемента {k} внутри {j}!","ERROR")
                        raw_pallete[i][j][k] = self.base_pallete[i][j][k]
                        continue

                    # проверка размера
                    if raw_pallete[i][j][k] < 0 or raw_pallete[i][j][k] > 255:
                        mainself.Log.write(f"Неверный размер данных элемента {k} внутри {j}!","ERROR")
                        raw_pallete[i][j][k] = self.base_pallete[i][j][k]
                        continue
                
        mainself.Log.write(f"Итоговая палитра:\n{raw_pallete}")
        
        return raw_pallete
