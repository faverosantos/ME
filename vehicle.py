
class Vehicle:
    id = 0
    len = 0
    position = 0
    velocity = 0
    type = "bird"

    def __init__(self):
        self.position = list()
        self.velocity = list()

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setLen(self, len):
        self.len = len

        # Se a versão de FW for igual ao antes a 3.13
        if self.len == 1:
            self.type = "pre-track"
        elif self.len == 1.2:
            self.type = "pedestrian"
        elif self.len == 2:
            self.type = "bicycle/motorcycle"
        elif self.len == 3.2:
            self.type = "undefined"
        elif 4.4 <= self.len <= 8.4:
            self.type = "passenger car"
        elif self.len > 8.5:
            self.type = "truck"
        else:
            self.type = "not listed"

    def getLen(self):
        return self.len

    def getClass(self):
        return self.type

    def setPosition(self, posX, posY):
        pair = (posX, posY)
        self.position.append(pair)

    def setVelocity(self, velX, velY):
        pair = (velX, velY)
        self.velocity.append(pair)

    def getPosition(self):
        return self.position

    def getVelocity(self):
        return self.velocity
