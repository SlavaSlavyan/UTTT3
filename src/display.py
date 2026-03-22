import pygame

class Display:

    def __init__(self, mainself):

        mainself.Log.write("Инициализация класса работы дисплея.","DEBUG")

        self.colors = mainself.Json.load(mainself,"data\\palette")

        self.reload_screen(mainself)

        mainself.Log.write(f"Начальные значения размера экрана {self.screen.get_size()}")
        mainself.Log.write(f"Начальные значения приближения = {self.zoom}")

        mainself.Log.write("Изменение иконки и заголовка дисплея","DEBUG")
        pygame.display.set_caption(f"Ulimate Tic Tac Toe")
        pygame.display.set_icon(pygame.image.load("data\\asset\\small_icon.png"))

        mainself.Log.write("Инициализация класса обработки времени отображения кадров.","DEBUG")
        self.Clock = pygame.time.Clock()

    def main(self, mainself):
        '''Отрисовка сцены и расчёт глобальных переменных для отрисовки'''

        self.fps = self.Clock.get_fps()
        if self.fps != 0: self.speed = 60/self.fps
        else: self.speed = 0

        exec(f"mainself.Scene.{mainself.status}.Display.main(mainself)")

        self.DebugText.main(mainself)

    def on_resize(self, mainself):
        '''
            Функция для перерисовки спрайтов если размер экрана был изменён.\n
            Обычно вызывается из класса Event.
        '''

        mainself.Log.write("Запущена функция перерисовки")

        self.width, self.height = self.screen.get_size()
        self.zoom = min(self.screen.get_size())/800

        mainself.Log.write(f"Новые значения размера экрана {self.screen.get_size()}")
        mainself.Log.write(f"Новые значения приближения = {self.zoom}")

        exec(f"mainself.Scene.{mainself.status}.Display.on_resize(mainself)")
    
    def reload_screen(self, mainself):

        mainself.Log.write("Обновление экрана!")
        
        if mainself.config["fullscreen"]:
            self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

        else:
            self.screen = pygame.display.set_mode(mainself.config["screen-size"],pygame.RESIZABLE)
        
        self.width, self.height = self.screen.get_size()
        self.zoom = min(self.screen.get_size())/800