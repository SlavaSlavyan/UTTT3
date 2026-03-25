import pygame

from util.mouse import Mouse
from util.keyboard import KeyBoard

class Event:

    def __init__(self, mainself):

        mainself.Log.write("Инициализация класса обработки событий.","DEBUG")
        
        self.Mouse = Mouse(mainself)
        self.KeyBoard = KeyBoard(mainself)

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
            self.KeyBoard.main(mainself, event)

        if self.KeyBoard.keys["fullscreen"]["press"]:

            mainself.Log.write("Изменение режима экрана.")

            if mainself.config["fullscreen"]:
                mainself.config["fullscreen"] = False
            else:
                mainself.config["fullscreen"] = True

            mainself.Display.reload_screen(mainself)
            mainself.Display.on_resize(mainself)
            
        exec(f"mainself.Scene.{mainself.status}.Logic.main(mainself)")
        
    def update(self, mainself):

        self.Mouse.update(mainself)
        self.KeyBoard.update(mainself)