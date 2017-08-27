# ******************************************************************************
# Name:    Pi calculations
# Author:  Vadim Korotkikh
# Description: Calcutate Pi
#
# ******************************************************************************
# Begin Imports

import math
from gmpy2 import mpz
from gmpy2 import isqrt
from time import time

def main():
	print("test")

#
def pi_chudnovsky_algo(digits):
	"""	Calculate Pi digits using Chudnovski series w/ binary splitting
		returns digits via mpz	"""
	c = 640320
	cto3_div24	= (c**3) // 24
	C3_OVER_24 = (c**3)// 24
	def binarysplit(a, b):
		"""
		Computes the terms for binary splitting the Chudnovsky infinite series

		a(a) = +/- (13591409 + 545140134*a)
		p(a) = (6*a-5)*(2*a-1)*(6*a-1)
		b(a) = 1
		q(a) = a*a*a*C3_OVER_24

		returns P(a,b), Q(a,b) and T(a,b)
		"""
		if b - a == 1:
			if a == 0:
				Pab = Qab = mpz(1)
			else:
				Pab = mpz((6*a-5)*(2*a-1)*(6*a-1))
				Qab = mpz(a*a*a*cto3_div24)
			Tab = Pab * ( 13591409 + 545140134*a)  # a(a) * p(a)
			if a & 1:
				Tab = -Tab
		else:
			# Recursively compute P(a,b), Q(a,b) and T(a,b)
			# m is the midpoint of a and b
			m = (a + b) // 2
			# Recursively calculate P(a,m), Q(a,m) and T(a,m)
			Pam, Qam, Tam = binarysplit(a,m)
			# Recursively calculate P(m,b), Q(m,b) and T(m,b)
			Pmb, Qmb, Tmb = binarysplit(m, b)
			# combine everything
			Pab = Pam * Pmb
			Qab = Qam * Qmb
			Tab = Qmb * Tam + Pam * Tmb
		return Pab, Qab, Tab
	# how many terms to compute
	DIGITS_PER_TERM = math.log10(C3_OVER_24/6/2/6)
	N = int(digits/DIGITS_PER_TERM + 1)
	# Calculate P(0,N) and Q(0, N)
	P, Q, T = binarysplit(0, N)
	one_squared = mpz(10)**(2*digits)
	sqrtC = isqrt(10005*one_squared)
	# returns an mpz class containing the pi digits...
	return (Q*426880*sqrtC) // T

# The last 5 digits or pi for various numbers of digits
check_digits = {
	100 : 70679,
	1000 :  1989,
	10000 : 75678,
	100000 : 24646,
	1000000 : 58151,
	# 10000000 : 55897,
}

if __name__ == "__main__":

	digits = 100
	try:
		print("# ***********************************************************************")
		print("# Name: Pie Number Calculator")
		print("# Author: Not I (not yet)")
		print("# Date:    Aug 2017	")
		print("#	")
		print("# ***********************************************************************")
		pi_chudnovsky_algo(sys.argv[1])
	except IndexError:
		print("# ***********************************************************************")
		print("# Name: Pie Number Calculator")
		print("# Author: Not I (not yet)")
		print("# Date:    Aug 2017	")
		print("#	")
		print("# ***********************************************************************")
		print("")
		piedigs = input("Enter number of Pie digits to calculate")
		pidig	= pi_chudnovsky_algo(digits)
		print("Data type:", type(pidig), "Length :D ?", len(pidig))
		print(pidig)

	#raise SystemExit in case of ...
	for log10_digits in range(1,9):
		digits 	= 10**log10_digits
		stime	= time()
		pi = pi_chudnovsky_algo(digits)
		print("Chudnovsky gmpy mpz algorithm")
		print("Digits:", digits, "exec time:", time() - stime)
		if digits in check_digits:
			last_five_digits = pi % 100000
			if check_digits[digits] == last_five_digits:
				print("Last five digits %05d OK" % last_five_digits)
			else:
				print("Last 5 digits %05d wrong should be %05d" % (last_five_digits, check_digits[digits]))
