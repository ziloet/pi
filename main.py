from decimal import Decimal, getcontext
from time import time

if(__name__ == "__main__"):
	print("How many digits to calculate?")
	NumDigits = int(input())
	Precision = NumDigits + 3	# round error guard digits

	Context = getcontext()
	Context.prec = Precision
	Context.Emax = 999999999

	StartTime = time()
	C = 426880 * Decimal(10005).sqrt()
	K = Decimal(6)
	M = Decimal(1)
	X = Decimal(1)
	L = Decimal(13591409)
	S = L

	for I in range(1, Precision):
		I3 = I * I * I
		K3 = K * K * K
		M *= (K3 - (16 * K)) / I3
		L += 545140134
		X *= -262537412640768000
		S += (M * L) / X
		K += 12
	Result = C / S
	Pi = str(Result)[0:-2]	# truncate guard digits
	print(Pi)
	EndTime = time()
	ElapsedTime = EndTime - StartTime
	print("\nTime elapsed: " + str(ElapsedTime) + " sec")
