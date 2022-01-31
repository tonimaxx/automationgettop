class human:

    def __init__(self, name):
        self.name = name
        self.basicpower = ["walk","run"]

    def username(self):
        return self.name

    def reversename(self):
        return (self.name)[::-1]

class superhuman(human):

    def __init__(self,name,universe):
        # human.__init__(self,name)
        super().__init__(name)
        self.superpower = []
        self.universe = universe

    def add_power(self,power):
        self.superpower.append(power)

    def total_power(self):
        return len(self.superpower)

    def all_power(self):
        return self.superpower


toni = superhuman("Jarus Soontornsing","marvel")
toni.add_power("fly")
toni.add_power("lightning")
print(toni.all_power())

print(toni.reversename())
print(toni.basicpower)
print(toni.universe)



# //
def can_see_park(a):
    buildingno = []
    b = a[::-1]
    tallest = 0
    for i,k in enumerate(b):
        if k > tallest:
            tallest = k
            buildingno.append(len(a)-i)
    return buildingno


test = [3, 5, 9, 6, 7, 5]
print(can_see_park(test))
