import traceback

class Scene:

    def __init__(self, mainself):

        mainself.Log.write("Инициализация класса загрузки сцен.","DEBUG")
        
        self.loaded_list = []
    
    def load(self, mainself, name:str):
        '''
            Загружает main класс заданной сцены в свой класс (Scene)
            - **name** [string]\n
                Одновременно *id* и *путь* загружаемого класса.
                Все сцены загружаются из директории *scene/{name}/main.py*
        '''

        mainself.Log.write(f"Загрузка сцены {name}.")
        
        #try:
            
        exec(f"from scene.{name.lower()}.main import {name};self.{name} = {name}(mainself);")
        
        if name in self.loaded_list:
            
            self.loaded_list.append(name)
            mainself.Log.write(f"Сцена {name} перезаписанна!")
        
        mainself.Log.write(f"Загрузка сцены {name} прошла успешно!")

        #except Exception as err:
        #    mainself.Log.write(f"Ошибка загрузки сцены {name}!\n{traceback.format_exc()}.","WARNING")