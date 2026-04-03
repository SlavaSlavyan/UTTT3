import pygame
import sys

from src.display import Display
from src.event import Event
from util.scene import Scene
from util.log import Log
from util.asset import Asset
from util.json import Json
from util.debugText import DebugText
from util.checkFile import CheckFile

class Program:
    '''Главный класс программы'''

    def __init__(self, version:str):
        '''- **version**: версия программы'''

        # подгружаем логи
        self.Log = Log()
        self.Log.write("Инициализация основного класса.","DEBUG")
        self.Log.write(f"Ultimate Tic Tac Toe версии {version} @SLL.","DEBUG")

        # подгружаем классы загрузки файлов программы и их проверку
        self.Json = Json(self)
        self.CheckFile = CheckFile(self)
        
        # переменные
        self.load_config() # конфиг игры
        self.version = version # версия игры
        self.status = "Game" # статус игры. Является ID сцен

        self.Log.write(f"Начальная сцена {self.status}.","DEBUG")
        self.Log.write(f"Инициализация pygame","DEBUG")

        pygame.init()

        self.Display = Display(self)
        self.Event = Event(self)
        self.Scene = Scene(self)
        self.Asset = Asset(self)
    
    def starter(self):
        '''Функция которая выполняется до запуска программы'''
        
        self.Log.write("==========START==========","DEBUG")

        self.Display.DebugText = DebugText(self)
        self.Asset.load(self,"Cursor")
        self.Display.Cursor = self.Asset.Cursor(self)
        self.Scene.load(self,"Game")

    def main(self):
        '''Основная функция программы. Выполняется внутри цикла.'''

        self.Event.main(self)

        self.Display.main(self)

        pygame.display.flip()

        self.Event.update(self)

        self.Display.Clock.tick(self.config["max-fps"])
        
    def load_config(self):
        '''Загрузка конфигурации'''
        
        self.Log.write("Загрузка конфигурации программы.")
        
        # базовые данные
        raw_config = self.Json.load(self,"data\\config")
        
        # проверка
        self.config = self.CheckFile.config(self, raw_config)
        
        # сохраняем данные
        self.Json.save(self,"data\\config",self.config)

    def stop(self):
        '''Функция для корректной остановки игры'''

        self.Json.save(self,"data\\config",self.config)
        self.Log.write("==========STOP==========","DEBUG")
        self.Log.save()
        
        pygame.quit()
        sys.exit()