from game.casting.actor import Actor

class Artifact(Actor):
    
    def __init__(self):
        super().__init__()
        self.message = ""
        self._points = 0

    def get_points(self):
        if (self.get_text() == '*'):
            self._points = 1
        else:
            self._points = -1

        return self._points
