# *************************************************************************************
x = int(input("Enter an integer value to be computed as a factorial: "))
q = x
while q > 2:
	y = (q*(q-1))
	q -= 2
	while q > 2:
		y *= (q*(q-1))
		q -= 2
	if q == 0:	
		print("The factorial of", x, "is", y)
while 0 < q <= 2:
	y *= q
	q -= 1
	print("The factorial of", x, "is", y)
if x < 0:
	print("The number is not positive")
# **************************************************************************************