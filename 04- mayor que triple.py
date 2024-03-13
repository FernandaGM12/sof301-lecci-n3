a = int ( input ("Ingrese número a: "))
b = int ( input ("Ingrese número b: "))
c = int ( input ("Ingrese número c: "))
if a > b:
    if a > c:
        m = a
    else:
        m = c
else: 
    if b > c:
        m = b
    else:
        m = c
print (m)