import pygame

class Display:

    def __init__(self, mainself):

        mainself.Log.write("Инициализация класса работы дисплея.","DEBUG")

        self.colors = {
            "global":{
                "version-text":(171, 178, 191)
            },
            "game":{
                "bg":(40, 44, 52),
                "rect-bg":(33, 37, 43),
                "line":(171, 178, 191)
            }
        }
        
        self.screen = pygame.display.set_mode((800,800),pygame.RESIZABLE)
        self.width, self.height = self.screen.get_size()
        self.zoom = min(self.screen.get_size())/800

        mainself.Log.write(f"Начальные значения размера экрана {self.screen.get_size()}")
        mainself.Log.write(f"Начальные значения приближения = {self.zoom}")

        mainself.Log.write("Инициализация класса обработки времени отображения кадров.","DEBUG")
        self.Clock = pygame.time.Clock()

        mainself.Log.write("Изменение иконки и заголовка дисплея","DEBUG")
        pygame.display.set_caption(f"Ulimate Tic Tac Toe {mainself.version}")
        pygame.display.set_icon(pygame.image.load("data\\assets\\small_icon.png"))

        mainself.Log.write("Создание поверхности текста версии игры","DEBUG")
        self.text_version = pygame.font.Font("data\\font\\base.otf",7).render(f"vers: {mainself.version}", False, self.colors["global"]["version-text"])
        self.text_version.set_alpha(255/4)

    def main(self, mainself):
        '''Отрисовка сцены и расчёт глобальных переменных для отрисовки'''

        self.fps = self.Clock.get_fps()
        if self.fps != 0: self.speed = 60/self.fps
        else: self.speed = 0

        exec(f"mainself.Scene.{mainself.status}.Display.main(mainself)")

        self.screen.blit(self.text_version,(self.width - self.text_version.get_width() - 5,
                                            self.height - self.text_version.get_height()))

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