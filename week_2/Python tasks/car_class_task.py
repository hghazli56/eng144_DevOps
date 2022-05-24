class Car:

    def __init__(self, top_speed, current_speed):
        self.top_speed = top_speed
        self.current_speed = current_speed

    def accelerate(self):
        if self.current_speed >= self.top_speed:
            return "You can't go any faster!"
        else:
            self.current_speed += 10
            return self.current_speed

    def brake(self):
        self.current_speed -= 30
        if self.current_speed <= 0:
            return"The car has stopped" 
        return self.current_speed


lambo = Car(200, 180)

print(lambo.accelerate())
print(lambo.accelerate())
print(lambo.accelerate())
print(lambo.accelerate())
print(lambo.accelerate())
print(lambo.accelerate())
print(lambo.accelerate())
print(lambo.accelerate())
print(lambo.accelerate())
print(lambo.brake())
print(lambo.brake())
print(lambo.brake())
print(lambo.brake())
print(lambo.brake())
print(lambo.brake())
print(lambo.brake())
print(lambo.brake())
print(lambo.brake())
print(lambo.brake())
print(lambo.brake())
print(lambo.brake())





