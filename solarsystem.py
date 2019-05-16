class System:

    def __init__(self):
        self.bodies = []
        

    def add(self, new_body):
        self.bodies.append(new_body)

    def total_mass(self):
        mass = 0
        for body in self.bodies:
            mass += body.mass
        return mass

      

class Body:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
    
    def __repr__(self):
        return self.name

class Planet(Body):
    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = year


class Star(Body):
    def __init__(self, name, mass, type_of):
        super().__init__(name, mass)
        self.type = type_of
        

class Moon(Body):
    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.month = month
        self.planet = planet

solar = System()
star = Body('star', 300)
planet = Body('planet', 5000)
solar.add(star)
solar.add(planet)
print(solar.total_mass())

sun = Star('Sun', 1.989, 'G' )
print(sun)
earth = Planet('Earth', 8484, 10, 2001)
moon = Moon('moon', 638398, 30, earth)
print(moon)
solar.add(moon)
solar.add(earth)
solar.add(sun)
print(solar.total_mass())
print(solar.bodies)
