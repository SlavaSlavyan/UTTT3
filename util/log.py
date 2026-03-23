# файл обработки логов

import os
from datetime import datetime

class Log:

    def __init__(self):

        self.path = "data\\log\\last.log"

        if os.path.exists(self.path):
            os.remove(self.path)

        self.last_logs = []
        
        self.save_value = 1

        self.write("==========INIT==========","DEBUG")
        
    def write(self, line:str, type:str = "INFO"):
        '''
            Пишет новый лог.
            - **line** [String]:\n 
                Информация лога.
            - **type** [String]:\n
                Тип лога. Изначально INFO, но можно написать любой.
        '''

        line = f"[{datetime.now().strftime("%H:%M:%S.%f")}][{type}] {line}"
        
        print(line)
        
        self.last_logs.append(line)

        if len(self.last_logs) > self.save_value:
            self.save()
            self.last_logs.clear()

    def save(self, path:str = "DEFAULT"):
        '''
            Сораняет массив логов, который находится в классе Log.
            - **path** [String]:\n
                Отвечает за путь в котором будет сохранён файл.
        '''

        if path == "DEFAULT":
            path = self.path

        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        
        with open(path, "a", encoding="utf-8") as file:

            for line in self.last_logs:
                file.write(line + '\n')