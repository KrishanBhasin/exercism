allergy_score = {1:'eggs', 2:'peanuts', 4:'shellfish',8:'strawberries',
                 16:'tomatoes',32:'chocolate',64:'pollen',128:'cats'}
				 #	USE BINARY!!!

actual_allergies = []

class MyAllergies:
    """a class that contains the 'is_allergic_to' method """
    allergies = []
    def is_allergic_to(allergen):
        if allergin in allergies:
            return True
        return False



def Allergies(num):
    testing_allergies = MyAllergies()
    
    for i in [2**n for n in range(7,-1,-1)]:
        if num-i>0:
            testing_allergies.allergies.append(allergy_score[i])
            num-=i
    if num==1:
            testing_allergies.allergies.append(allergy_score[1])

    return testing_allergies

###must be a class due to testing style
