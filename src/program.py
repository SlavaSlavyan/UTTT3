# основной файл. Ядро программы

import pygame
import sys
import time

from src.display import Display
from src.event import Event
from util.scene import Scene
from util.log import Log
from util.asset import Asset
from util.json import Json
from util.debugText import DebugText

class Program:

    def __init__(self, version:str):

        self.Log = Log()
        self.Log.write("Инициализация основного класса.","DEBUG")
        self.Log.write(f"Ultimate Tic Tac Toe версии {version} @SLL.","DEBUG")

        self.Json = Json(self)

        self.config = self.Json.load(self,"data\\config")
        self.version = version # версия игры
        self.status = "Game" # статус игры. Является ID сцен

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

        self.Display.DebugText = DebugText(self)
        
        self.Scene.load(self,"Game")

        while (True):

            self.Event.main(self)

            self.Display.main(self)

            pygame.display.flip()

            self.Event.update(self)

            self.Display.Clock.tick(self.config["max-fps"])

    def stop(self):
        '''Функция для корректной остановки игры'''

        self.Log.write("==========STOP==========","DEBUG")
        self.Log.save()

        pygame.quit()
        sys.exit()