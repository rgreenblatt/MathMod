
class Organism():
	def __init__(self, identification, pred, diffus, metabolic, maxdists, label, consume, ambientEnergyUse, lDose):
		#Unique label
		self.ID = identification
		self.name = label
		self.predation=pred
		self.diffusion=diffus
		self.metrate=metabolic
		self.maxdist=maxdists
		#Which IDs an organism consumes
		self.consumed = consume
		self.ld50 = lDose
		#True if it consumes ambient energy
		self.ambient= ambientEnergyUse
	def __str__(self):
        	return self.names[self.level]
	def __repr__(self):
        	return str(self)
