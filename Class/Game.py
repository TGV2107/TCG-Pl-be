class Game:
    
    def __init__(self):
        
        self.Playing = False
        
        self.Screen = "main"
        
        self.Screen_Background = (0,0,0)
    
    def getPlaying(self): return self.Playing
    
    def getScreen(self): return self.Screen
    
    def getBackground(self): return self.Screen_Background