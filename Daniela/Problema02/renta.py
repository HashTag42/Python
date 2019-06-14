'''
2.	Cree un programa que sea capaz de calcular el impuesto anual sobre la renta un número de veces que sea necesario, 
según indique el usuario. Considere para el cálculo que el impuesto de la renta es el 15% del salario anual imponible  
de cada persona. Adicionalmente, la renta está afecta a deducción en función del número de hijos de la persona, 
cuyo detalle se muestra en la siguiente tabla:

    # de hijos	deducción
    0	        0%
    1 o 2 	    5%
    más de 2	15%

El usuario ingresa la siguiente información para los cálculos: renta bruta mensual y número de hijos.

Por simplicidad, asuma que la renta anual imponible es el 80% de la renta bruta anual.
'''

TasaImpuestoALaRenta    = 0.15
TasaRentaAnualImponible = 0.80

def Deduccion(x):
    if (x < 1):
        return 0.00;
    if (x >= 1 and x <= 2):
        return 0.05;
    if (x > 2):
        return 0.15;


def CalculaImpuesto(RentaBrutaMensual, NumeroDeHijos):

    # Validar argumentos

    print ("Argumento: RentaBrutaMensual = ", RentaBrutaMensual)
    if (RentaBrutaMensual < 0):
        print ("Error: La RentaBrutaMensual debe ser mayor o igual a cero.")
    
    print ("Argumento: NumeroDeHijos = ", NumeroDeHijos)
    if (NumeroDeHijos < 0):
        print ("Error: El NumeroDeHijos debe ser mayor o igual a cero.")

    RentaBrutaAnual = RentaBrutaMensual * 12
    RentaAnualImponible = RentaBrutaAnual * TasaRentaAnualImponible
    ImpuestoALaRenta = RentaAnualImponible * TasaImpuestoALaRenta * (1 - Deduccion(NumeroDeHijos))

    print ("Impuesto a la Renta = ", ImpuestoALaRenta)










