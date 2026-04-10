from scene.game.displayData.animation import Animation
from scene.game.displayData.game import Game
from scene.game.displayData.winLabel import WinLabel

class Display:
    '''Класс отображения сцены игры'''

    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса отображения сцены Game.","DEBUG")

        # отображение анимаций
        self.Animation = Animation(mainself)

        # отображение процесса игры
        self.Game = Game(mainself)

        # отображение плашки выйгрыша
        self.WinLabel = WinLabel(mainself)

    def main(self, mainself):
        '''Отображение сцены Игры'''

        scene = mainself.Scene.Game

        # очищаем экран
        mainself.Display.screen.fill(mainself.Display.colors["game"]["bg"])
        
        if scene.status == 0:
            
            # отрисовываем анимацию появления
            self.Animation.main(mainself)
            
            # событие смены локального статуса
            if self.Animation.time <= 0:
                
                mainself.Log.write("Новый статус сцены Game. (1)")
                
                # меняем статус
                scene.status = 1
                
                # обнуляем таймер
                self.Animation.time = 0
                
                # меняем направление анимаций
                self.Animation.speed = 1

                # добавляем на задний план клетки
                mainself.Asset.Cells(mainself).draw(mainself,(0,0), canvas=scene.Bg.surface)

        if scene.status == 1 or scene.status == 2:

            # отрисовываем основную часть игры
            self.Game.main(mainself)
        
        if scene.status == 2:

            # отрисовываем плашку выйгрыша
            self.WinLabel.main(mainself)
            
            # событие смены локального статуса
            if self.WinLabel.time <= 0:
                
                mainself.Log.write("Новый статус сцены Game. (3)")
                
                # меняем статус
                scene.status = 3
                
                # чистим задник
                scene.Bg.resize(mainself)
                
                # очищаем все клетки
                for i in range(9):
                    for j in range(9):
                        mainself.Scene.Game.Logic.Game.cells[i][j] = None
        
        if scene.status == 3:
            
            # отрисовываем анимацию конца
            self.Animation.main(mainself)
            
            # отрсовываем фигуры
            self.Game.Figures.main(mainself)
            
            # рисуем табличку
            mainself.Scene.Game.Label.draw(mainself,1 - self.Animation.time)
            
            # событие смены СЦЕНЫ!
            if self.Animation.time >= 1:

                # тут на самом деле очень смешной момент, так как 
                del mainself.Scene.Game      
                mainself.Scene.load(mainself,"Game")
                

    def on_resize(self, mainself):
        '''Перерисовка всех спрайтов'''
        
        mainself.Log.write("Перерисовка сцены Game.")

        scene = mainself.Scene.Game
        
        # глобальные спрайты которые должны обновляться всегда
        scene.Bg.resize(mainself)
        scene.SmallCells.resize(mainself)
        
        # спрайты, обновляющиеся во время анимаций
        if scene.status == 0 or scene.status == 3:
            
            scene.LineHorizontal.resize(mainself)
            scene.LineVertical.resize(mainself)
            
            for i in range(4):
                scene.corners[i].resize(mainself)
        
        # спрайты, обновляющиеся вне анимаций
        if scene.status == 1 or scene.status == 2:

            # добавляем на задник клетки
            mainself.Asset.Cells(mainself).draw(mainself,(0,0), canvas=scene.Bg.surface)

            scene.Select.resize(mainself)

        # спрайты, обновляющиеся только во время игры
        if scene.status == 1:

            scene.Selecting0.resize(mainself)
            scene.SelectingX.resize(mainself)
            scene.UnablSelecting.resize(mainself)
        
        # по сути отлельный if для таблички выйгрыша
        if scene.status == 2:
            scene.Label.resize(mainself)
        
        # спрайты, обновляющиеся после первой анимации
        if scene.status > 0:
            
            scene.SmallCircle.resize(mainself)
            scene.SmallCross.resize(mainself)
            scene.BigCircle.resize(mainself)
            scene.BigCross.resize(mainself)