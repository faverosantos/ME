
class Object:
    id = 0
    len = 0
    position = list()
    velocity = list()

    def __init__(self):
        pass

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setLen(self, len):
        self.len = len

    def getLen(self):
        return self.len

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

    def __del__(self):
        pass

