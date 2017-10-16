def quotientAndRemainder(dividend,divisor):

    return (dividend // divisor, dividend % divisor)

myDividend = 11
myDivisor = 4
(myQuotient, myRemainder) = quotientAndRemainder(myDividend, myDivisor)

print("Quotient: ", myQuotient)
print("Remainder: ", myRemainder)