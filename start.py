# файл запуска

import turtle
import traceback

class SimpleDisplay:
    
    def __init__(self):
        
        turtle.hideturtle()
        turtle.bgcolor((0,0,0))
        turtle.pencolor((1,1,1))
        turtle.tracer(0)
        turtle.up()
        
        self.screen = turtle.Screen()
        self.screen.setup(width=800, height=600)
        self.screen.listen()
        
        self.screen.onkey(self.up, "Up") 
        self.screen.onkey(self.down, "Down")
        self.screen.onkey(self.increase, "+") 
        self.screen.onkey(self.decrease, "minus")  
        
        self.scroll = 0
        self.size = 8
        
    def main(self, text):
        
        self.data = self.load_log("data\\log\\last")
        self.data += text
        
        while True:
            self.update()
            
    def load_log(self, path):
        
        try:
            with open(f"{path}.log", "r", encoding="utf-8") as file:
                data = file.read()

            return data

        except:
            return "NO DATA FOUND"
    
    def update(self):
        
        turtle.clear()
        
        turtle.goto(0,self.screen.window_height()//2-60)
        turtle.write("UTTT CRASH!", align="center", font=("Consolas",40,"normal"))
        
        turtle.goto(-self.screen.window_width()//2+self.size,-self.screen.window_height()//2+self.scroll*self.size*2)
        turtle.write(self.data, font=("Consolas",self.size,"normal"))
        
        turtle.update()

    def up(self):
        if self.scroll != 0:
            self.scroll += 1
    
    def down(self):
        self.scroll -= 1
            
    def increase(self):
        self.size += 1
        
    def decrease(self):
        if self.size != 1:
            self.size -= 1
        
try:

    from src.program import Program

    Program = Program("DEV 3.0.6")
    
    Program.main()
    
except Exception as err:
    SimpleDisplay().main(traceback.format_exc())