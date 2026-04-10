class Animation:
    '''Класс отрисовки анимации'''

    def __init__(self, mainself):
        
        mainself.Log.write("Инициализация класса отображения анимации сцены Game.","DEBUG")
        
        # таймер 
        self.time = 1

        # скорость таймера
        self.speed = -1

    def main(self, mainself):
        '''Отрисовка анимации'''

        scene = mainself.Scene.Game

        # большая часть окна
        most = max(mainself.Display.width, mainself.Display.height)
        
        # нынешняя точка в анимации (расчитывается из квадрата таймера)
        time = self.time * self.time
        
        # рисуем задний фон
        scene.Bg.size = 1 - time
        scene.Bg.draw(mainself)
        
        # рисуем линии больших клеток
        scene.LineHorizontal.draw(mainself,(most*time,100))
        scene.LineHorizontal.draw(mainself,(-most*time,-100))
        scene.LineVertical.draw(mainself,(-100,most*time))
        scene.LineVertical.draw(mainself,(100,-most*time))

        # рисуем маленькие клетки
        for y in range(-1,2):
            for x in range(-1,2):
                
                size = "DEFAULT"

                # если клетка в середине, то мы не меняем её положение, а изменяем размер
                if not y and not x:
                    size = 1 - time

                # рисуем клетку
                scene.SmallCells.draw(mainself, (200*x + x*most*time,
                                                 200*y + y*most*time), size)

        # рисуем уголки выделения
        scene.corners[0].draw(mainself,(-375-most*time,375+most*time),(0,0))
        scene.corners[1].draw(mainself,(-375-most*time,-375-most*time),(0,1))
        scene.corners[2].draw(mainself,(375+most*time,-375-most*time),(1,1))
        scene.corners[3].draw(mainself,(375+most*time,375+most*time),(1,0))
        
        # изменение таймера
        self.time = self.time + self.speed/60*mainself.Display.speed