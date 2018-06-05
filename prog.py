"""
function = input('Enter a function: ')
func = function.split('x^')
for temp in func:
    print(temp)
    
"""
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
print('If there is a a^x function input it as pow(a,x)')
print('If there is an inverse sin(x) function input it as asin(x)')
print('If there is an inverse cos(x) function input it as acos(x)')
print('If there is an inverse tan(x) function input it as atan(x)')
print('If there is an inverse cot(x) function input it as acot(x)')
print('If there is an inverse sec(x) function input it as asec(x)')
print('If there is an inverse csc(x) function input it as acsc(x)')
print('Input x^ as x**')
print('Use the * to show multiplication. Ex: 3x^2 is 3*x**2')

function = input('Enter the function: ')
center = int(input('Enter the center: '))
order = 

range1 = int(2/0.001)
x = float(center-1)
fval = []
deltx = 0.001
tot=0
for i in range(0,range1):
    tot=float(eval(function))
    fval.append(tot)
    x+=0.001
print(fval[1000])

onederiv = []
valonederiv = 0.0
for i in range(0,len(fval)-1):
    valonederiv = (fval[i+1]-fval[i])/deltx
    onederiv.append(valonederiv)

twoderiv = []
valtwoderiv = 0.0
for i in range(0,len(onederiv)-1):
    valtwoderiv = (onederiv[i+1]-onederiv[i])/deltx
    twoderiv.append(valtwoderiv)

threederiv = []
valthreederiv = 0.0
for i in range(0,len(twoderiv)-1):
    valthreederiv = (twoderiv[i+1]-twoderiv[i])/deltx
    threederiv.append(valthreederiv)
    
fourderiv = []
valfourderiv = 0.0
for i in range(0,len(threederiv)-1):
    valfourderiv = (threederiv[i+1]-threederiv[i])/deltx
    fourderiv.append(valfourderiv)

fivederiv = []
valfivederiv = 0.0
for i in range(0,len(fourderiv)-1):
    valfivederiv = (fourderiv[i+1]-fourderiv[i])/deltx
    fivederiv.append(valfivederiv)

sixderiv = []
valsixderiv = 0.0
for i in range(0,len(fivederiv)-1):
    valsixderiv = (fivederiv[i+1]-fivederiv[i])/deltx
    sixderiv.append(valsixderiv)
    
sevenderiv = []
valsevenderiv = 0.0
for i in range(0,len(sixderiv)-1):
    valsevenderiv = (sixderiv[i+1]-sixderiv[i])/deltx
    sevenderiv.append(valsevenderiv)
    
eightderiv = []
valeightderiv = 0.0
for i in range(0,len(sevenderiv)-1):
    valeightderiv = (sevenderiv[i+1]-sevenderiv[i])/deltx
    eightderiv.append(valeightderiv)
    
ninederiv = []
valninederiv = 0.0
for i in range(0,len(eightderiv)-1):
    valninederiv = (eightderiv[i+1]-eightderiv[i])/deltx
    ninederiv.append(valninederiv)

tenderiv = []
valtenderiv = 0.0
for i in range(0,len(ninederiv)-1):
    valtenderiv = (ninederiv[i+1]-ninederiv[i])/deltx
    tenderiv.append(valtenderiv)


print("Coefficients of each order f u prime:")
