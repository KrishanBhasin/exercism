class School:
    def __init__(self, name):
        self.name = name
        self.db = {}
        
    def add(self, name, grade_number):
        if grade_number in self.db:
            self.db[grade_number].append(name)
        else:
            self.db[grade_number] = [name]
            
    def grade(self,grade_number):
        if grade_number in self.db:
            return self.db[grade_number]
        else:
            return set()
            
    def sort_single_grade(self,list_of_names):
        return sorted(list_of_names) 
    
    def sort(self):
    
        grades = []
        for number in self.db:
            grades.append(number)
            
        grades = sorted(grades)
        to_return = []
        for number in grades:
            to_return.append((number,tuple(self.db[number])))
        return(to_return)