from util.logger import get_logger_print
from src.constants import PROGRAM_VERSION
from src.program import Program

print = get_logger_print()

print("=" * 40 + "[START]" + "=" * 40 + '\n',
      time_formatting = False,
      log_level_formatting = False)

print(f"%IЗапущенна программа Ultimate Tic Tac Toe версии [{PROGRAM_VERSION}]. Автор - @SLL.")
print("%WВЕРСИЯ DEV НЕ ПРЕДНАЗНАЧЕНА ДЛЯ ПУБЛИЧНОГО ИСПОЛЬЗОВАНИЯ! ЭТО НЕ КОНЕЧНЫЙ ПРОДУКТ!")

if __name__ == "__main__":
    Program().main()
else:
    print("%FЗапуск программы не соответствует нормам. Конец работы.")