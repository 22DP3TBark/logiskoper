"""
Autors: Indriķis Teodors Barkāns
DP2-3
Programma pārbauda punkta koordinates figurai. Rinkim kur riņķa vidus punkts ir -4;3 un radiuss ir 2 cm

"""
import doctest
def check_koord(punkts_x, punkts_y: float) -> float:
    """
    Funkcija pārbauda punkta koordinates (punkta_x; punkta_y) Rinkim kur riņķa vidus punkts ir -4;3 un radiuss ir 2 cm

    parameters 
    -----------
    punkta_x : float
        punkta x koordinate Dekartu plakne.
    punkta_y : float
        punkta x koordinate Dekartu plakne. 

    returns
    --------------
    str 
        iekšā, uz līnijas, ārpuss

    >>> check_koord(-2,1)
    'ārpuss'
    >>> check_koord(-4,3)
    'iekšā'
    >>> check_koord(-2,3)
    'uz līnijas'
    >>> check_koord(-3,1.5)
    'uz līnijas'
    >>> check_koord(-5,2)
    'iekšā'
    >>> check_koord(0,0)
    'ārpuss'
    """
    import math
    vidus_x = -4
    vidus_y = 3 
    radiuss = 2 
    distance = math.sqrt((punkts_x-vidus_x)**2 + (punkts_y-vidus_y)**2)

    if distance<=radiuss:
        return "Iekšā"
    elif radiuss == distance:
        return "uz līnijas"
    else:
        return "ārpus"
    
     
    
doctest.testmod(verbose=True)

punkts_x = float(input("x: "))
punkts_y = float(input("y: "))

import math
vidus_x = -4
vidus_y = 3 
radiuss = 2 
distance = math.sqrt((punkts_x-vidus_x)**2 + (punkts_y-vidus_y)**2)

if distance<=radiuss:
    print("Iekšā")
elif radiuss == distance:
    print("uz līnijas")
else:
    print( "ārpus")
    
