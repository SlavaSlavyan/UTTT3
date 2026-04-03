import pygame

class Mouse:
    '''Обработка мыши'''

    def __init__(self, mainself):

        mainself.Log.write("Инициализация класса обработки мыши.","DEBUG")
        
        self.keys = {"lt":1, "md":2, "rt":3}

        mainself.Log.write("Начальные значения кнопок:")       
        for i in self.keys:

            self.keys[i] = {"id":self.keys[i], "press":False, "hold":False, "release":False}
            mainself.Log.write(f"    {i} = {self.keys[i]};")
        
        # keys содержит наименования кнопок мыши и каждая кнопка содержит несколько полей
        # 3 состояния нажатия и id, к которому привязана эта кнопка внутри pygame
        
        self.pos = pygame.mouse.get_pos()

    def main(self, mainself, event:pygame.event.EventType):
        '''Проверяет действия мыши и изменяет соответствующие переменные внутри класса.
        - **event**: Принимает в себя все события из модуля pygame.event через метот get()''' 

        # обновление переменной записывающей позицию мыши
        if event.type == pygame.MOUSEMOTION:
            self.pos = pygame.mouse.get_pos()
        
        # событие нажатия кнопки
        if event.type == pygame.MOUSEBUTTONDOWN:
                
            for i in self.keys: 
                if event.button == self.keys[i]["id"]:
                    
                    self.keys[i]["press"] = True
                    self.keys[i]["hold"] = True

                    mainself.Log.write(f"Зажата кнопка {i} на позиции {self.pos}.")

        # событие отжатия кнопки
        if event.type == pygame.MOUSEBUTTONUP:
                
            for i in self.keys: 
                if event.button == self.keys[i]["id"]:
                    
                    self.keys[i]["release"] = True
                    self.keys[i]["hold"] = False

                    mainself.Log.write(f"Отжата кнопка {i} на позиции {self.pos}.")

    def update(self, mainself):
        '''Обновление переменных press и release для каждой кнопки.'''

        for i in self.keys:

            self.keys[i]["press"] = False
            self.keys[i]["release"] = False