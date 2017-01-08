from math import ceil
import sys

def karatsuba(x, y):
    # base case, if x or y is a single digit, simply return the product xy
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y

    # find m, the maximum # of digits of x or y
    m = max(len(str(x)), len(str(y)))

    # calculate m/2, rounded up
    mby2 = m / 2

    # split the digit sequences about the middle
    a = x / 10**(mby2)
    b = x % 10**(mby2)
    c = y / 10**(mby2)
    d = y % 10**(mby2)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    abcd = karatsuba(a+b, c+d)

    adbc = abcd - ac - bd

    xy = (10**(2*mby2) * ac) + (10**mby2 * adbc) + bd

    return xy

# def karatsuba(x,y):
# 	"""Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
# 	if len(str(x)) == 1 or len(str(y)) == 1:
# 		return x*y
# 	else:
# 		n = max(len(str(x)),len(str(y)))
# 		nby2 = n / 2
#
# 		a = x / 10**(nby2)
# 		b = x % 10**(nby2)
# 		c = y / 10**(nby2)
# 		d = y % 10**(nby2)
#
# 		ac = karatsuba(a,c)
# 		bd = karatsuba(b,d)
# 		ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
#
#         	# this little trick, writing n as 2*nby2 takes care of both even and odd n
# 		prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
#
# 		return prod

def main():
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print("{} * {} = {} (recursive)".format(x, y, karatsuba(x, y)))
    print("{} * {} = {} (correct)".format(x, y, x * y))


if __name__ == "__main__":
    main()
