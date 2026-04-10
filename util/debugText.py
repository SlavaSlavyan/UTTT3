import pygame

TEXT_SIZE = [6,8] # множитель для размера поверхности текста
TEXT_INDENT = [8,8] # отступ текста от границы экрана
VERSION_TEXT_TRANSPARENCY = 255/4 # прозрачность текста версии
TIMER_SPEED = 1/15 # скорость обновления информации текста

class DebugText:
    '''Отрисовка информации отладки'''

    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса отладки.","DEBUG")

        # шрифт для отладки
        self.debug_font = pygame.font.Font("data\\font\\debug.otf",5)
        
        # генерация текста
        self.generate_version_text(mainself)
        self.generate_debug_text(mainself)
        
        # таймер обновления текста отладки
        self.reload_timer = 0

    def main(self, mainself):
        '''Отрисовка всех поверхностей'''

        display = mainself.Display
        
        # если включена отладка, то отрисовываем текст отладки
        if mainself.config["debug"]:
            self.draw_debug_text(mainself)
            return

        # отрисовываем версии в правом нижнем углу
        display.screen.blit(self.version_text,
                            (display.width - self.version_text_size[0],
                            display.height - self.version_text_size[1]))
        
    def generate_version_text(self, mainself):
        '''генерация текста версии программы'''

        # генерация поверхности
        self.version_text = self.debug_font.render(
            f"vers: {mainself.version}", False, mainself.Display.colors["global"]["version-text"])
        
        # делаем текст полупрозрачным
        self.version_text.set_alpha(VERSION_TEXT_TRANSPARENCY)

        # получаем размеры поверхности (для отрисовки)
        self.version_text_size = self.version_text.get_size()
        
        mainself.Log.write("Создана поверхность отрисовки версии.")
    
    def generate_debug_text(self, mainself):
        '''генерация текста отладки'''
        
        # лист всех строк внутри 
        self.debug_list = [
            {"str":"Version UTTT: ","link":"mainself.version","size":2},
            {"str":"Start screen size: ","link":"mainself.config['screen-size']","size":1},
            {"str":"Fullscreen: ","link":"mainself.config['fullscreen']","size":1},
            {"str":"Max FPS: ","link":"mainself.config['max-fps']","size":1},
            {"str":"Main status: ","link":"mainself.status","size":1},
            {"str":"Screen: ","link":"[mainself.Display.width, mainself.Display.height]","size":1},
            {"str":"Zoom: ","link":"round(mainself.Display.zoom,2)","size":1},
            {"str":"FPS: ","link":"round(mainself.Display.fps)","size":1},
            {"str":"Input mode: ","link":"mainself.Event.mode","size":1},
            {"str":"Mouse pos: ","link":"mainself.Event.Mouse.pos","size":1},
            {"str":"Win: ","link":"mainself.Scene.Game.Logic.Game.win","size":1},
        ]
        
        # содержит несколько полей
        # str: строчка которая пишется перед информацией (подпись)
        # link: ссылка на информацию
        # size: размер строки по Y
        # pos: позиция где нужно разместить информацию на экране
        
        # размеры текста
        text_len = [0,0]
        
        for line in self.debug_list:
            
            line["data"] = None
            
            # поиск размера по X
            if len(line["str"]) > text_len[0]:
                text_len[0] = len(line["str"])
            
            # поиск размера по Y
            text_len[1] += line["size"]

        # создаём поверхность для текста
        self.debug_text = pygame.Surface((text_len[0]*TEXT_SIZE[0],
                                          text_len[1]*TEXT_SIZE[1]),pygame.SRCALPHA)
        
        # координата строки по оси Y для отрисовки
        y = 0
        
        for line in self.debug_list:
            
            # создаём текст линии
            text = self.debug_font.render(line["str"], False, mainself.Display.colors["global"]["debug-text"])
            
            # отрисовываем
            self.debug_text.blit(text,(0, y * TEXT_SIZE[1]))
            
            # записываем позицию
            line["pos"] = (TEXT_INDENT[0] + text.get_width(),
                           TEXT_INDENT[1] + y * TEXT_SIZE[1])
            
            # добавляем отступ
            y += line["size"]
    
    def draw_debug_text(self, mainself):
        '''отрисовка текста отладки'''
        
        # убавляем таймер
        self.reload_timer -= TIMER_SPEED * mainself.Display.speed
        
        display = mainself.Display
        
        # отрисовываем начальный текст
        display.screen.blit(self.debug_text, TEXT_INDENT)
        
        for line in self.debug_list:
            
            # получаем информацию из ссылки
            try:
                result = {"mainself":mainself, "result":None}
                exec(f"result = {line['link']}",{},result)
                result = str(result["result"])
            except:
                result = "NO DATA FOUND"
            
            # обновляем данные
            if result != line["data"] and self.reload_timer <= 0:
                line['data'] = result
            
                # создаём поверхность
                line["surface"] = self.debug_font.render(result, False, mainself.Display.colors["global"]["debug-text"])
                
            # отрисовываем
            display.screen.blit(line["surface"],line["pos"])
        
        # обновление таймера
        if self.reload_timer < 0:
            self.reload_timer = 1