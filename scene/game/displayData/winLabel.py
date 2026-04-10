class WinLabel:
    '''Отображает информацию при победе одного из игроков'''

    def __init__(self, mainself):

        mainself.Log.write("Инициализация класса отображения победного экрана.","DEBUG")

        # размер таблички
        self.size = 1  

        # таймер
        # ВОТ ТУТ ДОДЕЛАТЬ!!!

    def main(self, mainself):
        '''отображает табличку'''
        
        # рисуем табличку
        self.Label.draw(mainself,1 - self.size)

        # изменяем размер
        self.size /= 1 + (0.1 * mainself.Display.speed)

    def create_label(self, mainself, win:int):
        '''Создаёт ассет победного экрана
        - **win**: значение выйгрыша'''

        # настраиваем табличку в зависимости от переменной

        if win == 0:
            color = mainself.Display.colors["game"]["circle"]
            string = "PLAYER 0 WIN"

        elif win == 1:
            color = mainself.Display.colors["game"]["cross"]
            string = "PLAYER X WIN"
        
        else:
            color = mainself.Display.colors["game"]["select-corner"]
            string = "DRAW"

        # создаём класс
        self.Label = mainself.Asset.Label(mainself,(600,200),string,color)