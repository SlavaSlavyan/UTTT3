# файл загрузки сцен

class Scene:

    def __init__(self, mainself):

        mainself.Log.write("Инициализация класса загрузки сцен.","DEBUG")
        
        self.load(mainself, "Game") # загрузка первой сцены
    
    def load(self, mainself, name:str):
        '''
            Загружает main класс заданной сцены в свой класс (Scene)
            - **name** [string]\n
                Одновременно *id* и *путь* загружаемого класса.
                Все сцены загружаются из директории *scene/{name}/main.py*
        '''

        mainself.Log.write(f"Загрузка сцены {name}.")
        
        try:
            exec(f"from scene.{name.lower()}.main import {name};self.{name} = {name}(mainself);")
            mainself.Log.write(f"Загрузка сцены {name} прошла успешно!")

        except Exception as err:
            mainself.Log.write(f"Ошибка загрузки сцены {name}!\nPython: {err}.","WARNING")