class Scene:

    def __init__(self, mainself):
        
        self.load(mainself, "Game")
    
    def load(self, mainself, name:str):

        exec(f"from scene.{name.lower()}.main import {name};self.{name} = {name}(mainself);")
