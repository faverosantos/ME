
class Vehicle:
    id = 0
    len = 0
    position = 0
    positionX = 0
    positionY = 0
    velocityX = 0
    velocityY = 0
    velocity = 0
    type = "bird"

    def __init__(self):
        self.position = list()
        self.velocity = list()
        self.positionX = list()
        self.positionY = list()
        self.velocityX = list()
        self.velocityY = list()

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

    def getPositionX(self):
        return self.positionX

    def getPositionY(self):
        return self.positionY

    def setPositionX(self, posX):
        self.positionX.append(posX)

    def setPositionY(self, posY):
        self.positionY.append(posY)

    def setPosition(self, posX, posY):
        pair = (posX, posY)
        self.position.append(pair)

    def setVelocity(self, velX, velY):
        pair = (velX, velY)
        self.velocity.append(pair)

    def setVelocityX(self, velX):
        self.velocityX.append(velX)

    def setVelocityY(self, velY):
        self.velocityY.append(velY)

    def getVelocityX(self):
        return self.velocityX

    def getVelocityY(self):
        return self.velocityY

    def getPosition(self):
        return self.position

    def getVelocity(self):
        return self.velocity
