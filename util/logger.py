import builtins
import types
import os

from datetime import datetime
from typing import cast

BASE_PRINT: types.FunctionType = builtins.print
BASE_LOG_PATH: str = "log\\_last.log"
BASE_LOG_LEVEL: str = "TRACE"

def set_logger_print() -> None:
    '''Переназначает встроенную функцию `print`, добавляя логирование.'''
    
    global print
    print = get_logger_print()

def get_logger_print() -> types.FunctionType:
    '''Возвращает переназначенную встроенную функцию `print`, добавляя логирование.'''

    def print(*args: object, 
              time_formatting: bool = True, 
              log_level_formatting: bool = True, 
              **kwargs: object):
        
        str_args: tuple[str, ...] = tuple(str(a) for a in args)
        sep: object = kwargs.get("sep", " ")
        end: object = kwargs.get("end", "\n")
        
        sep = cast(str, sep)
        end = cast(str, end)
        
        line: str = sep.join(str_args) + end
        
        if time_formatting:
            line = datetime.now().strftime("[%H:%M:%S.%f] ") + line
            
        if log_level_formatting:
            line = f"[{get_log_level(line)}] " + line
            
        if os.path.isdir(os.path.dirname(BASE_LOG_PATH)):
            
            try:
                with open(BASE_LOG_PATH, 'a', encoding="utf-8") as file:
                    file.write(line)
        
        BASE_PRINT(line)
        
    return print

def get_log_level(line: str) -> str:
    '''Получение уровня логирования из вложенной строчки для форматирования. 
Первые два символа в строке обозначают возвращаемый уровень.
- **%D** - debug\n- **%I** - info\n- **%W** - warn\n- **%E** - error\n- **%F** - fatal'''
    
    if line.startswith("%D"): return "DEBUG"
    
    elif line.startswith("%I"): return "INFO"
    
    elif line.startswith("%W"): return "WARN"
    
    elif line.startswith("%E"): return "ERROR"
    
    elif line.startswith("%F"): return "FATAL"
    
    else: return BASE_LOG_LEVEL