import traceback

from util.logger import get_logger_print, BASE_LOG_PATH
from util.simpleDisplay import SimpleDisplay
from src.constants import PROGRAM_VERSION
from src.program import Program

print = get_logger_print()

print("=" * 40 + "[START]" + "=" * 40 + '\n',
      time_formatting = False,
      log_level_formatting = False)

print(f"%IЗапущенна программа Ultimate Tic Tac Toe версии [{PROGRAM_VERSION}]. Автор - @SLL.")
print("%WВЕРСИЯ DEV НЕ ПРЕДНАЗНАЧЕНА ДЛЯ ПУБЛИЧНОГО ИСПОЛЬЗОВАНИЯ! ЭТО НЕ КОНЕЧНЫЙ ПРОДУКТ!")

if __name__ == "__main__":
    try:
        Program().main()
        
    except SystemExit:
        raise
        
    except:
        print("%FКритический сбой в программе!")
        SimpleDisplay.crash_log(BASE_LOG_PATH, traceback.format_exc())
else:
    print("%FЗапуск программы не соответствует нормам. Конец работы.")