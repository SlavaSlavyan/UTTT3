import json

class Json:

    def __init__(self, mainself):

        mainself.Log.write("Инициализация класса работы с Json файлами.","DEBUG")

    def load(self, mainself, path:str):
        '''
            Возвращает информацию из файла с расширением json
            - **path** [String]:\n
                Отвечает за путь файла из которого будет загружена информация.
        '''

        mainself.Log.write(f"Загрузка данных из файла {path}.json")

        with open(f"{path}.json", "r", encoding="utf-8") as file:
            data =  json.load(file)

        mainself.Log.write(f"Загрузка данных из файла {path}.json прошла успешно! Полученная информация:\n{data}")

        return data

# with open("data.json", "w", encoding="utf-8") as file:
#    json.dump(data, file, indent=4, ensure_ascii=False)
