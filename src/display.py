import pygame
import traceback

class Display:
    '''Обработка визуала'''

    def __init__(self, mainself):

        mainself.Log.write("Инициализация класса работы дисплея.","DEBUG")

        # загружаем цвета
        self.load_colors(mainself)

        # создаём класс окна
        self.reload_screen(mainself)

        # настраиваем pygame
        self.load_base_pygame_settings(mainself)

        mainself.Log.write("Инициализация класса обработки времени отображения кадров.","DEBUG")
        self.Clock = pygame.time.Clock()

    def main(self, mainself):
        '''Отрисовка сцены и расчёт глобальных переменных для отрисовки'''

        # обновление переменной фпс
        self.fps = self.Clock.get_fps()

        # обновление скорости анимации
        if self.fps != 0: self.speed = 60/self.fps
        else: self.speed = 0

        # вызов функции отрисовки рабочей сцены
        exec(f"mainself.Scene.{mainself.status}.Display.main(mainself)")

        # отрисовка отладочного текста
        self.DebugText.main(mainself)

        # отрисовка курсора
        self.Cursor.draw(mainself)

    def on_resize(self, mainself):
        '''Функция для перерисовки спрайтов если размер экрана был изменён.\n
        Обычно вызывается из класса Event.'''

        mainself.Log.write("Запущена функция перерисовки")

        # перезапись размера экрана
        self.width, self.height = self.screen.get_size()

        # новые значения приближения
        self.zoom = min(self.screen.get_size())/800

        mainself.Log.write(f"Новые значения размера экрана {self.screen.get_size()}")
        mainself.Log.write(f"Новые значения приближения = {self.zoom}")

        # вызов перерисовки внутри рабочей сцены
        exec(f"mainself.Scene.{mainself.status}.Display.on_resize(mainself)")
    
    def reload_screen(self, mainself):
        '''Функция обновления экрана\n
        Обновляет экран в зависимости от переменной **mainself.config["fullscreen"]**'''

        mainself.Log.write("Обновление экрана!")

        # перезапись класса экрана

        # полный экран
        if mainself.config["fullscreen"]:
            self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) 

        # растягивающийся экран
        else:
            self.screen = pygame.display.set_mode(mainself.config["screen-size"],pygame.RESIZABLE)
        
        # обновлене переменных размера и приближения
        self.width, self.height = self.screen.get_size()
        self.zoom = min(self.screen.get_size())/800

        mainself.Log.write(f"Начальные значения размера экрана {self.screen.get_size()}")
        mainself.Log.write(f"Начальные значения приближения = {self.zoom}")
    
    def load_colors(self, mainself):
        '''Загрузка палитры'''
        
        mainself.Log.write("Загрузка палитры.")
        
        # базовые данные
        raw_colors = mainself.Json.load(mainself,"data\\palette")
        
        # проверка
        self.colors = mainself.CheckFile.pallete(mainself, raw_colors)
        
        # сохраняем данные
        mainself.Json.save(mainself,"data\\palette",self.colors)

    def load_base_pygame_settings(self, mainself):
        '''Загружает настройки pygame связанные с отображением'''

        mainself.Log.write("Изменение иконки и заголовка дисплея","DEBUG")

        # ставим имя
        pygame.display.set_caption(f"Ultimate Tic Tac Toe")

        # скрываем мышку системы
        pygame.mouse.set_visible(False)

        # пытаемся загрузить иконку
        try: pygame.display.set_icon(pygame.image.load("data\\asset\\small_icon.png"))
        
        # возврат ошибки
        except Exception as err:
            mainself.Log.write(f"Ошибка загрузки иконки окна!\n{traceback.format_exc()}.","ERROR")