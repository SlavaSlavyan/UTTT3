class CheckFile:
    '''Класс проверки файлов программы'''
    
    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса проверки файлов программы.","DEBUG")
        
        # константы ПРАВИЛЬНЫХ файлов для восстановления
        
        # конфиг
        self.base_config = {
            "screen-size":[800,800],
            "fullscreen":False,
            "max-fps":-1,
            "debug":True
        }
        
        # бинд клавиш
        self.base_bind = {
            "input":13,
            "up":1073741906,
            "down":1073741905,
            "left":1073741904,
            "right":1073741903,
            "fullscreen":1073741892,
            "debug":1073741884
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
            
            if raw_config["screen-size"][i] < 300:
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
        
        if raw_config["max-fps"] < 10 and raw_config["max-fps"] != -1:
            mainself.Log.write(f"Неверный размер данных max-fps!","ERROR")
            raw_config["max-fps"] = self.base_config["max-fps"]
            
        # ОТЛАДКА
        if not isinstance(raw_config["debug"], bool):
            mainself.Log.write(f"Неверный тип данных debug!","ERROR")
            raw_config["debug"] = self.base_config["debug"]
        
        mainself.Log.write(f"Итоговая конфигурация:\n{raw_config}")
            
        return raw_config

    def bind(self, mainself, raw_bind):
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