from math import pow

def on_square(num):
	return int(pow(2,num-1))

def total_after(num):
	sum = 0
	for i in range(1,num+1):
		sum += on_square(i)
		
	return sum