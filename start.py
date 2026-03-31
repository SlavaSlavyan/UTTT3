import os
import traceback
import tkinter

from tkinter import font

class SimpleDisplay:
    '''Простой дисплей для отрисовки ошибок'''
    
    def __init__(self, error_text:str):
        '''- **error_text**: лог ошибки которую надо вывести'''
        
        self.error_text = error_text
        
        # настройка окна
        self.root = tkinter.Tk()
        self.root.title("Ultimate Tic Tac Toe crash")
        self.root.geometry("800x600")
        
        # шрифт текста (для удобного изменения размера)
        self.font = font.Font(family="Consolas", size=8) 
        
        # бинд клавиш
        self.root.bind("-", lambda e: self.change_size(-2))
        self.root.bind("_", lambda e: self.change_size(-2))
        self.root.bind("+", lambda e: self.change_size(2))
        self.root.bind("=", lambda e: self.change_size(2))
        
        # пробуем загрузить иконку для окна
        try:
            icon = tkinter.PhotoImage(file='data\\asset\\small_icon.png')
            self.root.iconphoto(False, icon)
        except:
            pass

    def main(self):
        '''Отрисовка экрана'''

        # создаём поверхность для текста
        frame = tkinter.Frame(self.root)
        frame.pack(expand=True, fill='both')

        # создаём полоску прокрутки
        scrollbar = tkinter.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')

        # создаём текст используя созданный шрифт
        text = tkinter.Text(frame, wrap='word', yscrollcommand=scrollbar.set, bg='black', fg='white', font=self.font)
        text.pack(side='left', expand=True, fill='both')

        # биндим скролл текста
        scrollbar.config(command=text.yview)
        
        # отрисовываем текст
        text.insert('end', self.error_text)
        
        # запускаем основной цикл окна
        self.root.mainloop()
        
    def load_log(path:str) -> str:
        '''Загрузка лога. Возвращает строки лога
        - **path**: путь до файла'''
        
        try:
            with open(path,"r",encoding='utf-8') as file:
                return file.read()
            
        # в случае ошибки вернёт ненаход
        except:
            return "NO LOG DATA FOUND\n"
        
    def change_size(self, delta:int):
        '''Динамическое изменение размера текста.\n
        Функция используется в бинде клавиш
        - **delta**: число которое будет прибавленно к текущему размеру'''
        
        # получаем нынешний размер шрифта
        current_size = self.font.actual("size")
        
        # ставим новый
        new_size = max(8, current_size + delta)
        self.font.configure(size=new_size)
        
        
# удаляем старый лог    
if os.path.exists("data\\log\\last.log"):
    os.remove("data\\log\\last.log")
        
try:

    from src.program import Program

    # экземпляр основного класса
    Program = Program("DEV 3.0.8")
    
    Program.starter()
    
    # основной цикл
    while True:
        Program.main()
    
except Exception as err:
    
    # Лог создаётся из полученной информации из файла последнего лога и самой ошибки
    log = SimpleDisplay.load_log("data\\log\\last.log") + traceback.format_exc()
    SimpleDisplay(log).main()