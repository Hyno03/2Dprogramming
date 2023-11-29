class Npc:
    def __init__(self, x, y, size):
        self.x, self.y, self.size = x,y,size

npc1 = Npc(1,2,4.5)
npc2 = Npc(100,300,2.5)

print(type(npc1.__dict__))
print(npc1.__dict__)

npc1.x = 100
npc1.__dict__.update({'x' :500})

print(type(npc1.__dict__))
print(npc1.__dict__)

