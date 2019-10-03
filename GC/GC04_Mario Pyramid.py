PyramidNumber = int(input("Choose a number to build a pyramid."))
for i in range (PyramidNumber):
    print(' '*(PyramidNumber-i-1) + '*'*(2*i+1))
