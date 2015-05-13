class SpaceAge:
	def __init__(self, age):
		self.seconds = age
		self.seconds_in_earth_year  = 31557600
		self.seconds_in_mercury_year = 0.2408467 * self.seconds_in_earth_year
		self.seconds_in_venus_year_year = 0.61519726 * self.seconds_in_earth_year
		self.seconds_in_mars_year = 1.8808158 * self.seconds_in_earth_year
		self.seconds_in_jupiter_year_year = 11.862615 * self.seconds_in_earth_year
		self.seconds_in_saturn_year = 29.447498 * self.seconds_in_earth_year
		self.seconds_in_uranus_year = 84.016846 * self.seconds_in_earth_year
		self.seconds_in_neptune_year = 164.79132 * self.seconds_in_earth_year	
	
	def on_earth(self):
		ans = self.seconds/self.seconds_in_earth_year
		return float('%.2f' % ans)
		
	def on_mercury(self):
		ans = self.seconds/self.seconds_in_mercury_year
		return float('%.2f' % ans)
	def on_venus(self):
		ans = self.seconds/self.seconds_in_venus_year_year
		return float('%.2f' % ans)
	def on_mars(self):
		ans = self.seconds/self.seconds_in_mars_year
		return float('%.2f' % ans)
	def on_jupiter(self):
		ans = self.seconds/self.seconds_in_jupiter_year_year
		return float('%.2f' % ans)
	def on_saturn(self):
		ans = self.seconds/self.seconds_in_saturn_year
		return float('%.2f' % ans)
	def on_uranus(self):
		ans = self.seconds/self.seconds_in_uranus_year
		return float('%.2f' % ans)
	def on_neptune(self):
		ans = self.seconds/self.seconds_in_neptune_year
		return float('%.2f' % ans)