import traceback

class Asset:
    '''Хранилище ассетов'''

    def __init__(self, mainself):

        mainself.Log.write("Инициализация класса загрузки ассетов.","DEBUG")
        
        # список всех загруженных ассетов
        self.loaded_list = []
    
    def load(self, mainself, name:str):
        '''Загружает класс ассета в свой класс (Asset)
        - **name**: название класса который нужно импортировать.\n 
        Загрузка происходит из директории *data.asset.{name}.py*'''

        mainself.Log.write(f"Загрузка ассета {name}.")
        
        try:
            
            # если не загружен
            if name not in self.loaded_list:

                exec(f"from data.asset.{name.lower()} import {name};self.{name} = {name};")
                self.loaded_list.append(name)
                
                mainself.Log.write(f"Загрузка ассета {name} прошла успешно!")
                return

            mainself.Log.write(f"Ассет {name} уже загружен!", "ERROR")

        except Exception as err:
            mainself.Log.write(f"Ошибка загрузки ассета {name}!\n{traceback.format_exc()}.","WARNING")