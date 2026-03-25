import pygame

class DebugText:

    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса отладки.","DEBUG")

        self.debug_font = pygame.font.Font("data\\font\\debug.otf",5)
        
        self.create_version_text(mainself)
        self.generate_debug_text(mainself)

    def main(self, mainself):

        display = mainself.Display
        
        if mainself.config["debug"]:
        
            self.draw_debug_text(mainself)

        else:
            display.screen.blit(self.version_text,
                                (display.width - self.version_text_size[0],
                                display.height - self.version_text_size[1]))
        
    def create_version_text(self, mainself):

        self.version_text = self.debug_font.render(
            f"vers: {mainself.version}", False, mainself.Display.colors["global"]["version-text"])
        
        self.version_text.set_alpha(255/4)

        self.version_text_size = self.version_text.get_size()
        
        mainself.Log.write("Создана поверхность отрисовки версии.")
    
    def generate_debug_text(self, mainself):
        
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
        ]
        
        text_len = [0,0]
        
        for line in self.debug_list:
            
            if len(line["str"]) > text_len[0]:
                text_len[0] = len(line["str"])
            
            text_len[1] += line["size"]

        self.debug_text = pygame.Surface((text_len[0]*6,text_len[1]*8),pygame.SRCALPHA)
        
        y = 0
        
        for line in self.debug_list:
            
            text = self.debug_font.render(line["str"], False, mainself.Display.colors["global"]["debug-text"])
            
            self.debug_text.blit(text,(0,y*8))
            
            line["pos"] = (8 + text.get_width(),8+y*8)
            
            y += line["size"]
    
    def draw_debug_text(self, mainself):
        
        display = mainself.Display
        
        display.screen.blit(self.debug_text,(8,8))
        
        for line in self.debug_list:
            
            try:
                result = {"mainself":mainself, "result":None}
                exec(f"result = {line['link']}",{},result)
                result = str(result["result"])
            except:
                result = "NO DATA FOUND"
            
            
            text = self.debug_font.render(result, False, mainself.Display.colors["global"]["debug-text"])
            
            display.screen.blit(text,line["pos"])