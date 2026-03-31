import pygame

class KeyBoard:
    '''Обработка клавиатуры'''

    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса обработки клавиатуры.","DEBUG")

        # загрузка биндов из файла
        self.keys = mainself.Json.load(mainself,"data\\bind") 

        mainself.Log.write("Начальные значения клавиш:")
        for i in self.keys:

            self.keys[i] = {"id":self.keys[i], "press":False, "hold":False, "release":False}
            mainself.Log.write(f"    {i} = {self.keys[i]};")
        
        # keys содержит наименования клавиш и каждая клавиша содержит несколько полей
        # 3 состояния нажатия и id, к которому привязана эта клавиша внутри pygame
        # то есть работает также как и обработка мыши

    def main(self, mainself, event:pygame.event.EventType):
        '''Проверяет действия клавиатуры и изменяет соответствующие переменные внутри класса.
        - **event**: Принимает в себя все события из модуля pygame.event через метот get()''' 

        # события нажатия клавиши
        if event.type == pygame.KEYDOWN:
                
            for i in self.keys: 
                if event.key == self.keys[i]["id"]:
                    
                    self.keys[i]["press"] = True
                    self.keys[i]["hold"] = True

                    mainself.Log.write(f"Зажата клавиша {i} [{self.keys[i]["id"]}]")

        # события отжатия клавиши
        if event.type == pygame.KEYUP:
                
            for i in self.keys: 
                if event.key == self.keys[i]["id"]:
                    
                    self.keys[i]["release"] = True
                    self.keys[i]["hold"] = False

                    mainself.Log.write(f"Отжата клавиша {i} [{self.keys[i]["id"]}]")

    def update(self, mainself):
        '''Обновление переменных press и release для каждой клавиши.\n
        Вызывается в классе Event после выполнения всей логики.'''

        for i in self.keys:

            self.keys[i]["press"] = False
            self.keys[i]["release"] = False