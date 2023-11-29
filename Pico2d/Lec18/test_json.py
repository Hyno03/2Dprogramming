import pickle

class Npc:
    def __init__(self, name, x, y, size):
        self.name, self.x, self.y, self.size = name,x,y,size

npc1 = Npc('jenny', 1,2,4.5)
npc2 = Npc('jisu', 100,300,2.5)

group = [npc1, npc2]
with open('npc.pickle', 'wb') as f:
    pickle.dump(group, f)
