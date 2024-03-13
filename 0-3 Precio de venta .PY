pv = float (input ( "Ingrese el precio de venta: "))
print ("Ingrese N para nacional o E para extranjero")
opcion = input ()
if opcion == "N":#ponerle las comillas 
    total = pv + (pv * 0.08)
else: 
    total = pv + (pv * 0.18)
print (" El total es: " + str(total))

