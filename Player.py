class Player:

    x_pos = None
    y_pos = None

    def __init__(self, xPos, yPos):
        self.x_pos = xPos
        self.y_pos = yPos

    def move_horizontal(self, amount):
        self.x_pos += amount

