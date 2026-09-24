import pygame
import sys

from util.logger import get_logger_print

class Program:
    '''Главный класс программы'''
    
    def __init__(self) -> None:
        print("%DИнициализация главного класса программы.")
        
        pygame.init()
    
    def main(self) -> None:
        '''Запуск программы'''
        
        self.stop()
    
    def stop(self) -> None:
        '''Остановка программы'''
        
        print("=" * 41 + "[END]" + "=" * 41,
              time_formatting = False,
              log_level_formatting = False)
        
        pygame.quit()
        sys.exit(0)

# Костыль, чтобы интерпретатор не ругался
print = get_logger_print()