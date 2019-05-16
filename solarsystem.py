class System:

    all_bodies = []

    def __init__(self):
        self.bodies = []

    @classmethod
    def total_galactic_mass(cls):
        mass = 0
        for body in cls.all_bodies:
            mass += body.mass
        return mass

        

    # def add(self, new_body):
        
    #     if new_body in self.bodies:
    #             print('this body is already in list')
    #     else:
    #          self.bodies.append(new_body)
    #          System.all_bodies.append(new_body)


    def add(self, new_body):
        if new_body.name in [body.name for body in self.bodies]:
            print('this body is already in list')
        else:
             self.bodies.append(new_body)
             System.all_bodies.append(new_body)

    def total_mass(self):
        mass = 0
        for body in self.bodies:
            mass += body.mass
        return mass

        # def add(self, new_body):
        # if len(self.bodies) == 0:
        #     self.bodies.append(new_body)
        #     System.all_bodies.append(new_body)
        # else:
        #     for body in self.bodies:
        #         if body.name == new_body.name:
        #             print('this body is already in list')
                            
        #         else: 
        #             self.bodies.append(new_body)
        #             System.all_bodies.append(new_body)
        #             break

      

class Body:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
    
    def __repr__(self):
        return self.name

    @classmethod
    def all(cls, system):
        bodies_list = []
        for body in system.bodies:
            # print('---',type(body))
            if isinstance(body,cls):
                bodies_list.append(body)
        return bodies_list

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
alpha = System()
star2 = Body('star2', 600)
planet2 = Body('planet2', 2000)
alpha.add(star2)
alpha.add(planet2)

star = Body('star', 300)
planet = Body('planet', 5000)
solar.add(star)
solar.add(planet)
print(solar.total_mass())

sun = Star('Sun', 1.989, 'G' )
sun1 = Star('Sun1', 1.989, 'G' )
print(sun)
earth = Planet('Earth', 8484, 10, 2001)
jupiter = Planet('Jupiter', 9999, 11, 2004)
moon = Moon('moon', 638398, 30, earth)
print(moon)
solar.add(moon)
solar.add(earth)
solar.add(jupiter)
solar.add(sun)
solar.add(sun)
print(solar.total_mass())
print(solar.bodies)
solar.add(sun)
print(alpha.bodies)
print(System.all_bodies)
print(System.total_galactic_mass())

print(Planet.all(solar))


# print(Body.all(['h','y',10],str))