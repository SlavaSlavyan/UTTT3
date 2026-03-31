import os
from datetime import datetime

class Log:
    '''Работа с логами'''

    def __init__(self):

        self.path = "data\\log\\last.log" # Путь для сохранения лога
        self.last_logs = []               # Временное хранилище логов
        self.save_value = 1               # Максимальное количество логов во временном хранилище

        self.write("==========INIT==========","DEBUG")
        
    def write(self, line:str, type:str = "INFO"):
        '''Пишет новый лог.
        - **line**: Информация лога.
        - **type**: Тип лога. Изначально INFO'''

        # форматирование строчки (добавление времени и типа)
        line = f"[{datetime.now().strftime("%H:%M:%S.%f")}][{type}] {line}"
        print(line)
        
        # сохранение во временное хранилище
        self.last_logs.append(line)

        # разгрузка хранилища
        if len(self.last_logs) > self.save_value:
            self.save()
            self.last_logs.clear()

    def save(self):
        '''Сораняет массив логов, который находится в классе Log.
        - **path**: Отвечает за путь в котором будет сохранён файл.'''

        # если путь не существует, то создаёт его
        if not os.path.exists(os.path.dirname(self.path)):
            os.makedirs(os.path.dirname(self.path))
        
        # добавление всех строк в файл
        with open(self.path, "a", encoding="utf-8") as file:

            for line in self.last_logs:
                file.write(line + '\n')