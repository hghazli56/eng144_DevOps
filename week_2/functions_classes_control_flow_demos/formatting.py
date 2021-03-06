class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return(f"Location(latitude = {self.latitude}, longitude = {self.longitude})")#allows us to format how class is presented

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"#str will take priority over repr

bham_academy = Location(52.488674, -1.887249)
#print(bham_academy)

n = 0.004837

print(f"Fixed Point: {n:f}")
print(f"Exponential Notation: {n:e}")
