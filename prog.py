#program used for estimating value of function using tenth order taylor polynomial
#note that if consecutive derivatives of f(x) reach 0 before the tenth derivative the estimation may contain large amounts of eror due to limitations of numerical differentiation
import math

if __name__ == '__main__':
    data = {}
    data['coefficients'] = ''
    data['derivative'] = ''
print('If there is a sinx function input it as sin(x)')
print('If there is a cosx function input it as cos(x)')
print('If there is a tanx function input it as tan(x)')
print('If there is a cotx function input it as cot(x)')
print('If there is a secx function input it as sec(x)')
print('If there is a cscx function input it as csc(x)')
print('If there is a log(x)/log(base) function input it as log(x[,base]')
print('If there is an lnx function input it as log(x)')
print('If there is a e^x function input it as exp(x)')
print('If there is an inverse sin(x) function input it as asin(x)')
print('If there is an inverse cos(x) function input it as acos(x)')
print('If there is an inverse tan(x) function input it as atan(x)')
print('If there is an inverse cot(x) function input it as acot(x)')
print('If there is an inverse sec(x) function input it as asec(x)')
print('If there is an inverse csc(x) function input it as acsc(x)')
print('Input x^ as x**')
print('Use the * to show multiplication. Ex: 3x^2 is 3*x**2')
sin(x) = math.sin(x)
cos(x) = math.cos(x)
tan(x) = math.tan(x)
cot(x) = math.cot(x)
sec(x) = math.sec(x)
csc(x) = math.csc(x)
log(x) = math.log(x)
exp(x) = math.exp(x)
asin(x) = math.asin(x)
acos(x) = math.acos(x)
atan(x) = math.atan(x)
acot(x) = math.acot(x)
asec(x) = math.asec(x)
acsc(x) = math.acsc(x)

function = input('Enter the function: ')
center = int(input('Enter the center: '))
value = float(input('Evaluated at: '))

#calculates values of original function over interval (center-1,center+1)
range1 = int(2/0.001)
x = float(center-1)
fval = []
deltx = 0.001
tot=0
for i in range(0,range1):
    tot=float(eval(function))
    fval.append(tot)
    x+=0.001

#calculates values of first derivative over interval (center-1,center+1)
onederiv = []
valonederiv = 0.0
for i in range(0,len(fval)-1):
    valonederiv = (fval[i+1]-fval[i])/deltx
    onederiv.append(valonederiv)

#calculates values of second derivative over interval (center-1,center+1)
twoderiv = []
valtwoderiv = 0.0
for i in range(0,len(onederiv)-1):
    valtwoderiv = (onederiv[i+1]-onederiv[i])/deltx
    twoderiv.append(valtwoderiv)

#calculates values of third derivative over interval (center-1,center+1)
threederiv = []
valthreederiv = 0.0
for i in range(0,len(twoderiv)-1):
    valthreederiv = (twoderiv[i+1]-twoderiv[i])/deltx
    threederiv.append(valthreederiv)

#calculates values of fourth derivative over interval (center-1,center+1)
fourderiv = []
valfourderiv = 0.0
for i in range(0,len(threederiv)-1):
    valfourderiv = (threederiv[i+1]-threederiv[i])/deltx
    fourderiv.append(valfourderiv)

#calculates values of fifth derivative over interval (center-1,center+1)
fivederiv = []
valfivederiv = 0.0
for i in range(0,len(fourderiv)-1):
    valfivederiv = (fourderiv[i+1]-fourderiv[i])/deltx
    fivederiv.append(valfivederiv)

#calculates values of sixth derivative over interval (center-1,center+1)
sixderiv = []
valsixderiv = 0.0
for i in range(0,len(fivederiv)-1):
    valsixderiv = (fivederiv[i+1]-fivederiv[i])/deltx
    sixderiv.append(valsixderiv)

#calculates values of seventh derivative over interval (center-1,center+1)
sevenderiv = []
valsevenderiv = 0.0
for i in range(0,len(sixderiv)-1):
    valsevenderiv = (sixderiv[i+1]-sixderiv[i])/deltx
    sevenderiv.append(valsevenderiv)

#calculates values of eighth derivative over interval (center-1,center+1)
eightderiv = []
valeightderiv = 0.0
for i in range(0,len(sevenderiv)-1):
    valeightderiv = (sevenderiv[i+1]-sevenderiv[i])/deltx
    eightderiv.append(valeightderiv)

#calculates values of ninth derivative over interval (center-1,center+1)
ninederiv = []
valninederiv = 0.0
for i in range(0,len(eightderiv)-1):
    valninederiv = (eightderiv[i+1]-eightderiv[i])/deltx
    ninederiv.append(valninederiv)

#calculates values of tenth derivative over interval (center-1,center+1)
tenderiv = []
valtenderiv = 0.0
for i in range(0,len(ninederiv)-1):
    valtenderiv = (ninederiv[i+1]-ninederiv[i])/deltx
    tenderiv.append(valtenderiv)

#calculates values of each order's taylor coeffecient using consecutive derivatives at the center and the factorial denominator 
I0 = fval[1000]/1
I1 = onederiv[1000]/1
I2 = twoderiv[1000]/2
I3 = threederiv[1000]/6
I4 = fourderiv[1000]/24
I5 = fivederiv[1000]/120
I6 = sixderiv[1000]/720
I7 = sevenderiv[1000]/5040
I8 = eightderiv[1000]/40320
I9 = ninederiv[1000]/362880
I10 = tenderiv[1000]/3628800

C0 = str(fval[1000]/1)
C1 = str(onederiv[1000]/1)
C2 = str(twoderiv[1000]/2)
C3 = str(threederiv[1000]/6)
C4 = str(fourderiv[1000]/24)
C5 = str(fivederiv[1000]/120)
C6 = str(sixderiv[1000]/720)
C7 = str(sevenderiv[1000]/5040)
C8 = str(eightderiv[1000]/40320)
C9 = str(ninederiv[1000]/362880)
C10 = str(tenderiv[1000]/3628800)

print("Coefficients of each order:")
print(str("C0: ")+str(C0))
print(str("C1: ")+str(C1))
print(str("C2: ")+str(C2))
print(str("C3: ")+str(C3))
print(str("C4: ")+str(C4))
print(str("C5: ")+str(C5))
print(str("C6: ")+str(C6))
print(str("C7: ")+str(C7))
print(str("C8: ")+str(C8))
print(str("C9: ")+str(C9))
print(str("C10: ")+str(C10))

#calculates value of estimation with Taylor's formula
fvalue = I0*((value-center)**0)+I1*((value-center)**1)+I2*((value-center)**2)+I3*((value-center)**3)+I4*((value-center)**4)+I5*((value-center)**5)+I6*((value-center)**6)+I7*((value-center)**7)+I8*((value-center)**8)+I9*((value-center)**9)+I10*((value-center)**10)

print(str("f(")+str(value)+str("): ") + str(fvalue))
