import pickle

class Npc:
    def __init__(self, name, x, y, size):
        self.name, self.x, self.y, self.size = name,x,y,size

with open('npc.pickle', 'rb') as f:
    group = pickle.load(f)

for o in group:
    print(type(o), o.name, o.x, o.y, o.size)