import pygame

class DebugText:

    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса отладки.","DEBUG")

        self.debug_font = pygame.font.Font("data\\font\\debug.otf",5)
        
        self.create_version_text(mainself)

    def main(self, mainself):

        display = mainself.Display

        display.screen.blit(self.version_text,
                            (display.width - self.version_text_size[0],
                            display.height - self.version_text_size[1]))
        
    def create_version_text(self, mainself):

        self.version_text = self.debug_font.render(
            f"vers: {mainself.version}", False, mainself.Display.colors["global"]["version-text"])
        
        self.version_text.set_alpha(255/4)

        self.version_text_size = self.version_text.get_size()
        
        mainself.Log.write("Создана поверхность отрисовки версии.")