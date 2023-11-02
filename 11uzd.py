"""
Autors:  Indrīķis Teodors Barkāns
DP2-3
Programma pārbauda punkta koordinates figurai. Trapeces koordinātes ir -3;2, -2,5;8 , 4;8, 8,2;2 
"""
 
import doctest

def check_coordinates(punkts_x, punkts_y: float) -> str:
    """
    Funkcija pārbauda punkta koordinates (punkta_x; punkta_y) figūrai Trapecei ar koordinātēm -3;2, -2.5;8, 4;8, 8.2;2

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

    >>> check_coordinates(1,1)
    'ārpuss'
    >>> check_coordinates(4,4)
    'iekšā'
    >>> check_coordinates(-3,2)
    'uz līnijas'
    >>> check_coordinates(1,8)
    'uz līnijas'
    >>> check_coordinates(6,5.1)
    'uz līnijas'
    >>> check_coordinates(-4,3)
    'ārpuss'
    """
    if punkts_x > -3 and punkts_x < 8.2 and punkts_y > 2 and punkts_y < 8 or punkts_y > 12 * punkts_x + 38 and punkts_y < 1.428571 * punkts_x + 13.714:
        return "iekšā"
    elif punkts_x == -3 or punkts_x == 8.2 or punkts_y == 2 or punkts_y == 8 or punkts_y == 12 * punkts_x + 38 or punkts_y == 1.428571 * punkts_x + 13.714:
        return "uz līnijas"
    else:
        return "ārpuss"

   
doctest.testmod(verbose=True)

punkts_x = float(input("Ievadiet x Koordināti: "))
punkts_y = float(input("Ievadiet y Koordināti: "))

if punkts_x > -3 and punkts_x < 8.2 and punkts_y > 2 and punkts_y < 8 or punkts_y > 12 * punkts_x + 38 and punkts_y < 1.428571 * punkts_x + 13.714:
    print("iekšā")
elif punkts_x == -3 or punkts_x == 8.2 or punkts_y == 2 or punkts_y == 8 or punkts_y == 12 * punkts_x + 38 or punkts_y == 1.428571 * punkts_x + 13.714:
    print("uz līnijas")
else:
    print("ārpuss")
