class Rect:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def intersect(self, rect: 'Rect') -> bool:
        # TODO: implement me

        if ((self.x + self.width <= rect.x) or (self.y + self.height <= rect.y)) or ((rect.x + rect.width <= self.x) or (rect.y + rect.height <= self.y)):
            return False
        else:
            return True
