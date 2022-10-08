from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

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

    # def set_message(self, message):
        # self.message = message
# 
    # def get_message(self):
        # return self.message