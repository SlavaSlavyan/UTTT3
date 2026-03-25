# файл отвечающий за обработку мыши

import pygame

class Mouse:

    def __init__(self, mainself):

        mainself.Log.write("Инициализация класса обработки мыши.","DEBUG")

        self.keys = {"lt":1, "md":2, "rt":3}

        mainself.Log.write("Начальные значения кнопок:")
        
        for i in self.keys:

            self.keys[i] = {"id":self.keys[i], "press":False, "hold":False, "release":False}
            mainself.Log.write(f"    {i} = {self.keys[i]};")
        
        self.pos = pygame.mouse.get_pos()
        
        # каждый элемент keys это dict с полями 
        # "id" [int] - определённый номер соответсвующий номеру кнопки мыши внутри pygame
        # "press" [bool] - проверка нажатия кнопки
        # "hold" [bool] - проверка зажатия кнопки
        # "release" [bool] - проверка отжатия кнопки

    def main(self, mainself, event:pygame.event.EventType):
        '''
            Проверяет действия мыши и изменяет соответствующие переменные внутри класса.
            - **event** [Event]:\n 
                Принимает в себя все события из модуля pygame.event через метот get()
        ''' 

        if event.type == pygame.MOUSEMOTION:

            self.pos = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
                
            for i in self.keys: 
                if event.button == self.keys[i]["id"]:
                    
                    self.keys[i]["press"] = True
                    self.keys[i]["hold"] = True

                    mainself.Log.write(f"Зажата кнопка {i} на позиции {self.pos}.")

        if event.type == pygame.MOUSEBUTTONUP:
                
            for i in self.keys: 
                if event.button == self.keys[i]["id"]:
                    
                    self.keys[i]["release"] = True
                    self.keys[i]["hold"] = False

                    mainself.Log.write(f"Отжата кнопка {i} на позиции {self.pos}.")

    def update(self, mainself):
        '''
            Обновление переменных press и release для каждой кнопки.\n
            Вызывается в классе Event после выполнения всей логики.
        '''

        for i in self.keys:

            self.keys[i]["press"] = False
            self.keys[i]["release"] = False