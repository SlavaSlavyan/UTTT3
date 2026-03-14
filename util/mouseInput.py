# class responsible for handling mouse clicks
# subclass of Event

import pygame

class Mouse:

    def __init__(self, mainself):

        self.keys = {"lt":1, "md":2, "rt":3}

        for i in self.keys:

            self.keys[i] = {"id":self.keys[i], "press":False, "hold":False, "release":False}

    def main(self, mainself, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
                
            for i in self.keys: 
                if event.button == self.keys[i]["id"]:
                    
                    self.keys[i]["press"] = True
                    self.keys[i]["hold"] = True

        if event.type == pygame.MOUSEBUTTONUP:
                
            for i in self.keys: 
                if event.button == self.keys[i]["id"]:
                    
                    self.keys[i]["release"] = True
                    self.keys[i]["hold"] = False

    def update(self, mainself):

        for i in self.keys:

            self.keys[i]["press"] = False
            self.keys[i]["release"] = False