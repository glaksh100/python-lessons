def isPrime(num):
	#To check if a number is prime
	factors=0
	for i in range(2,num):
		if(num%i==0):
			factors=factors+1
	if(factors==0):
		is_Prime=True
	else:
		is_Prime=False
	return is_Prime

#print isPrime(15)