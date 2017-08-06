# ******************************************************************************
# Name:    Pi calculations
# Author:  Vadim Korotkikh
# Description: Calcutate Pi
#
# ******************************************************************************
# Begin Imports

import math
from gmpy2 import mpz
from time import time

def main():
	print("test")


def pi_chudnovsky_algo(digits):

	c = 640320
	# cto3_div24	= (c**3) // 24
	C3_OVER_24 = (c**3)// 24
    def binarsplit(a, b):
        """
        Computes the terms for binary splitting the Chudnovsky infinite series

        a(a) = +/- (13591409 + 545140134*a)
        p(a) = (6*a-5)*(2*a-1)*(6*a-1)
        b(a) = 1
        q(a) = a*a*a*C3_OVER_24

        returns P(a,b), Q(a,b) and T(a,b)
        """
		if b - a == 0:
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
			Pam, Qam, Tam = binarsplit(a,m)
			Recursively calculate P(m,b), Q(m,b) and T(m,b)
            Pmb, Qmb, Tmb = binarsplit(m, b)
			# combine everything
			Pab = Pam * Pmb
			Qab = Qam * Qmb
			Tab = Qmb * Tam + Pam * Tmb
		return Pab, Qab, Tab

if __name__ == "__main__":
	main()
