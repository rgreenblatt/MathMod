
class Organism():
    predations=(0.9,0.5,0.4)
    diffusions=(0.05,0.2,0.15)
    metabolics=(0.2,0.3,0.4)
    distances=(2,3,5)
    names=("Plant","Fish","Osprey")
    def __init__(self,level):
        self.level=level
        self.predation=self.predations[level]
        self.diffusion=self.diffusions[level]
        self.metrate=self.metabolics[level]
        self.maxdist=self.distances[level]
    def __str__(self):
        return self.names[self.level]
    def __repr__(self):
        return str(self)
