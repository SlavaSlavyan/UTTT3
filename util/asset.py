# класс загрузки ассетов

class Asset:

    def __init__(self, mainself):

        mainself.Log.write("Инициализация класса загрузки ассетов.","DEBUG")
        
        self.loaded_list = []
    
    def load(self, mainself, name:str):
        '''
            Загружает класс ассета в свой класс (Asset).
            - **name** [string]\n
                Одновременно *id* и *путь* загружаемого класса.
                Все ассеты загружаются из директории *data/asset/{name}.py*
        '''

        mainself.Log.write(f"Загрузка ассета {name}.")
        
        #try:
            
        if name not in self.loaded_list:
    
            exec(f"from data.asset.{name.lower()} import {name};self.{name} = {name};")
            
            self.loaded_list.append(name)
            
            mainself.Log.write(f"Загрузка ассета {name} прошла успешно!")
        
        else:
            mainself.Log.write(f"Ассет {name} уже загружен!", "WARNING")

        #except Exception as err:
        #    mainself.Log.write(f"Ошибка загрузки ассета {name}!\nPython: {err}.","WARNING")