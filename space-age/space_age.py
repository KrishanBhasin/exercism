class SpaceAge:
	def __init__(self, age):
		self.seconds = age
		self.seconds_in_earth_year  = 31557600

		self.age_db = {
		'on_earth': 1.0,
		'on_mercury': 0.2408467,
		'on_venus': 0.61519726,
		'on_mars': 1.8808158,
		'on_jupiter': 11.862615,
		'on_saturn': 29.447498,
		'on_uranus': 84.016846,
		'on_neptune': 164.79132
		}
		
	def __getattr__(self,name):
		def age_calculation():
			return round((self.seconds/self.seconds_in_earth_year)/self.age_db[name],2)
	
		self.case = self.age_db.get(name)
		if not self.case:
			raise AttributeError
		return age_calculation
