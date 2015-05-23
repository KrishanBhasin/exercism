class Luhn:
    """
    A class to calculate and verify numbers against the Luhn Formula
    """
    def __init__(self, num):
        self.input = num
        self.addEndsList = []
        
    def LuhnDouble(self,to_double):
        """
        Handles numbers that exceed 9 during the 'doubling' phase of the Luhn Formula
        """
        doubled = to_double*2
        if doubled > 9:
            doubled -= 9
        return doubled
        
    def addends(self):
        """
        iterates through the provided number, doubling every second digit, starting from the RHS
        """
        self.input = str(self.input) #convert to string so we can cycle through it digit by digit
        for i in range(1,len(self.input)+1):
            if i%2==0:
                self.doubled_value = self.LuhnDouble(int(self.input[-i]))
                self.addEndsList.append(self.doubled_value)
            else:
                self.non_doubled_value = int(self.input[-i])
                self.addEndsList.append(self.non_doubled_value)
        return self.addEndsList #return a list containing the calculated values after every second digit has been 'doubled'
        
    def checksum(self):
        list_after_adding = self.addends()
        return int(str(sum(list_after_adding))[-1])#return only the last digit of the checksum calculation
        
    def is_valid(self):
        if self.checksum() == 0:
            return True
        return False
    
    @staticmethod
    def create(num_in):
        #add a '0' to the end of the string, to ensure the correct digits are doubled
        #(Luhns formula counts checkdigit as the first digit, so if this '0' is not added
        #then the wrong digits are doubled)
        checkitem = Luhn.checksum(Luhn(int( str(num_in)+'0')))
        
        #the '0' we added is expected to be incorrect - we now create checkdigit to be the number required
        #to ensure the sum ends in a zero
        checkdigit = 10 - checkitem
        num_out = int( str(num_in)+ str(checkdigit)[-1])

        return num_out