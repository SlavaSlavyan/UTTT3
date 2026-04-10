class WinLabel:
    '''Отображает информацию при победе одного из игроков'''

    def __init__(self, mainself):

        mainself.Log.write("Инициализация класса отображения победного экрана.","DEBUG")

        # размер таблички
        self.size = 1  

        # таймер
        self.time = 3

    def main(self, mainself):
        '''отображает табличку'''
        
        # рисуем табличку
        mainself.Scene.Game.Label.draw(mainself,1 - self.size)

        # изменяем размер
        self.size /= 1 + (0.1 * mainself.Display.speed)
        
        # отнимаем время от таймера
        self.time -= 1/60*mainself.Display.speed

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
        mainself.Scene.Game.Label = mainself.Asset.Label(mainself,(600,200),string,color)