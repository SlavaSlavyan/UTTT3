import json
import traceback

class Json:
    '''Обработчик файлов json'''

    def __init__(self, mainself):
        mainself.Log.write("Инициализация класса работы с Json файлами.","DEBUG")

    def load(self, mainself, path:str):
        '''Возвращает информацию из файла с расширением json.\n
        В случае ошибки вернёт спец символ '$'
        - **path**: Отвечает за путь файла из которого будет загружена информация.'''
        
        mainself.Log.write(f"Загрузка данных из файла {path}.json")

        try:

            with open(f"{path}.json", "r", encoding="utf-8") as file:
                data =  json.load(file)

            mainself.Log.write(f"Загрузка данных из файла {path}.json прошла успешно! Полученная информация:\n{data}")

            return data

        except Exception as err:
            
            mainself.Log.write(f"Ошибка загрузки файла {path}.json!\n{traceback.format_exc()}.","ERROR")
            return "$"

# будующий код для загрузки информации в файл

# with open("data.json", "w", encoding="utf-8") as file:
#    json.dump(data, file, indent=4, ensure_ascii=False)
