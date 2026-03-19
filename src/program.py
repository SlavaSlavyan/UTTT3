# основной файл. Ядро программы

import pygame
import sys

from src.display import Display
from src.event import Event
from util.scene import Scene
from util.log import Log
from util.asset import Asset

class Program:

    def __init__(self, version:str):

        self.Log = Log()
        self.Log.write("Инициализация основного класса.","DEBUG")

        self.version = version # версия игры
        self.status = "Game" # статус игры. Является ID сцен

        self.Log.write(f"Ultimate Tic Tac Toe версии {version} @SLL.","DEBUG")
        self.Log.write(f"Начальная сцена {self.status}.","DEBUG")
        self.Log.write(f"Инициализация pygame","DEBUG")

        pygame.init()

        self.Display = Display(self)
        self.Event = Event(self)
        self.Scene = Scene(self)
        self.Asset = Asset(self)

    def main(self):
        '''Основная функция программы, которая запускает основной цикл'''

        self.Log.write("==========START==========","DEBUG")
        
        self.Scene.load(self,"Game")

        while (True):

            self.Event.main(self)

            self.Display.main(self)

            pygame.display.flip()

            self.Display.Clock.tick(60)

    def stop(self):
        '''Функция для корректной остановки игры'''

        self.Log.write("==========STOP==========","DEBUG")
        self.Log.save()

        pygame.quit()
        sys.exit()