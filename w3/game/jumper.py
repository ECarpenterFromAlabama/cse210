class Jumper:
    
    def __init__(self):
        self.parachute = [" ___ ", \
                          "/___\\", \
                          "\   /", \
                          " \ / "
                          ]
        self.person = ["  O  ", \
                       " /|\ ", \
                       " / \ ", \
                       "     ", \
                       "^^^^^"
                       ]

    def draw_jumper(self):
        for i in self.parachute:
            print(i)
        for i in self.person:
            print(i)

    def remove_part(self):
        if(len(self.parachute) != 0):
            self.parachute.pop(0)
        if(len(self.parachute) == 0 ):
            self.person[0] = "  X  "