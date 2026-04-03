import pygame

from util.mouse import Mouse
from util.keyboard import KeyBoard

class Event:
    '''Класс обработки событий'''

    def __init__(self, mainself):

        mainself.Log.write("Инициализация класса обработки событий.","DEBUG")
        
        # подклассы обработки ввода
        self.Mouse = Mouse(mainself)
        self.KeyBoard = KeyBoard(mainself)
        
        # режим ввода
        self.mode = "MOUSE"

    def main(self, mainself):
        '''отвечает за все происходящие события в pygame'''
        
        # основной цикл
        for event in pygame.event.get():

            # обработка события выхода
            if event.type == pygame.QUIT:

                mainself.Log.write("Пользователь запустил событие выхода! Запуск функции выхода...")
                mainself.stop() # функция остановки игры в main классе

            # обработка события изменения размера окна
            if event.type == pygame.VIDEORESIZE:

                mainself.Log.write("Пользователь изменил размер экрана! Запуск функции перерисовки...")
                mainself.Display.on_resize(mainself) # функция изменения размера в display классе
            
            # обработка ввода
            self.Mouse.main(mainself, event)
            self.KeyBoard.main(mainself, event)

        # событие изменения режима экрана
        if self.KeyBoard.keys["fullscreen"]["press"]:
            self.fullscreen(mainself)
        
        # событие изменения режима отладки
        if self.KeyBoard.keys["debug"]["press"]:
            self.debug(mainself)
        
        # Выполнение логики из сцены
        exec(f"mainself.Scene.{mainself.status}.Logic.main(mainself)")
        
    def fullscreen(self, mainself):
        '''Изменение режима экрана'''

        mainself.Log.write("Изменение режима экрана.")

        # изменяем значения в конфиге
        if mainself.config["fullscreen"]:
            mainself.config["fullscreen"] = False
        else:
            mainself.config["fullscreen"] = True

        mainself.Display.reload_screen(mainself) # изменяем режим экрана
        mainself.Display.on_resize(mainself) # перерисовываем спрайты
    
    def debug(self, mainself):
        '''Изменение режима отладки'''
        
        # просто меняем значение в конфиге
        
        if mainself.config["debug"]:
            mainself.config["debug"] = False
            mainself.Log.write("Отладка выключена.")
            
        else:
            mainself.config["debug"] = True
            mainself.Log.write("Отладка включена.")
    
    def update(self, mainself):
        '''Обновление значений клавиш.\n
        *Вызывается внутри главного класса после отрисовки!*'''

        self.Mouse.update(mainself)
        self.KeyBoard.update(mainself)