import pygame

from util.mouse import Mouse

class Event:

    def __init__(self, mainself):

        mainself.Log.write("Инициализация класса обработки событий.","DEBUG")
        
        self.Mouse = Mouse(mainself)

    def main(self, mainself):
        '''отвечает за все происходящие события в pygame'''
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                mainself.Log.write("Пользователь запустил событие выхода! Запуск функции выхода...")
                mainself.stop()

            if event.type == pygame.VIDEORESIZE:

                mainself.Log.write("Пользователь изменил размер экрана! Запуск функции перерисовки...")
                mainself.Display.on_resize(mainself)
            
            self.Mouse.main(mainself, event)
        
        self.Mouse.update(mainself)