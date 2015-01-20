class Garden():
	
	def __init__(self,lines_of_plants, students = None):
		self.line1, self.line2 = lines_of_plants.split("\n")
		self.plant_dict = {
		'V':'Violoets',
		'R':'Radishes',
		'C':'Clover',
		'G':'Grass'
		}
		#if students == None:
		#	students = ['A','B','C','D','E','F','G','H','I','J','K','L']
	
	def plants(self,name):
		self.name = name[0]
		answer_letters = []
		answer_words = []
		for letter in self.line1:
			answer_letters.append(letter)
		for letter in self.line2:
			answer_letters.append(letter)
		for entry in answer_letters:
			answer_words.append(self.plant_dict[entry])
		return answer_words