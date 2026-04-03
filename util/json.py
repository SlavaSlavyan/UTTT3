import json
import traceback
import os

class Json:
    '''Обработчик файлов json'''

    def __init__(self, mainself):
        mainself.Log.write("Инициализация класса работы с Json файлами.","DEBUG")

    def load(self, mainself, path:str) -> any:
        '''Возвращает информацию из файла с расширением json.\n
        В случае ошибки вернёт спец символ '$'
        - **path**: Отвечает за путь файла из которого будет загружена информация.'''
        
        mainself.Log.write(f"Загрузка данных из файла {path}.json")

        try:

            # читаем иформацию
            with open(f"{path}.json", "r", encoding="utf-8") as file:
                data =  json.load(file)

            mainself.Log.write(f"Загрузка данных из файла {path}.json прошла успешно! Полученная информация:\n{data}")

            return data
        
        except Exception as err:
            
            mainself.Log.write(f"Ошибка загрузки файла {path}.json!\n{traceback.format_exc()}.","ERROR")
            return "$" # спец символ
        
    def save(self, mainself, path:str, data:any):
        '''Записывает информацию в файл с расширением json.\n
        Перезаписывает файл если он существует!
        - **path**: Отвечает за путь файла в который будет загружена информация.
        - **data**: Данные которые нужно записать.'''
        
        # добавляем расширение файла к пути
        path = path + ".json"
        
        mainself.Log.write(f"Загрузка данных в файл {path}. Загружаемые данные:\n{data}")
        
        # если путь не существует, то создаёт его
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
            
        # удаляем старый файл    
        if os.path.exists(path):
            os.remove(path)

        # записываем информацию
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            
        mainself.Log.write(f"Загрузка данных в файл {path} прошла успешно!")
