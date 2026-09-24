import tkinter as tk
from tkinter import scrolledtext
import traceback

BG_COLOR = "#1e1e1e"
FONT_COLOR = "#d4d4d4"
SELECT_COLOR = "#652678"

class SimpleDisplay:
    '''Создание простых окон для разных целей'''
    
    @staticmethod
    def crash_log(path: str, error: str) -> None:
        '''Создаёт окно с логом при краше игры'''
        
        root = tk.Tk()
        root.title("Ultimate Tic Tac Toe CRASH")
        root.geometry("900x600")
        root.configure(bg=BG_COLOR)
        
        text = scrolledtext.ScrolledText(
            root, wrap="none", font=("Consolas", 10),
            bg=BG_COLOR, fg=FONT_COLOR, insertbackground=FONT_COLOR,
            selectbackground=SELECT_COLOR, highlightthickness=0, borderwidth=0)
        
        text.pack(fill="both", expand=True)
        
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as f:
                text.insert("1.0", f.read() + error)
                
            with open(path, "a", encoding="utf-8", errors="replace") as f:
                f.write(error)
        except:
            text.insert("1.0", "НЕ УДАЛОСЬ ЗАГРУЗИТЬ ЛОГ! Причина:\n" + traceback.format_exc() + "\nПричина краша программы:\n" + error)
            
        text.see("end")
        text.configure(state="disabled")
        
        tk.mainloop()