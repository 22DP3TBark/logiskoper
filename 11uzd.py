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
    >>> check_coordinates(0,8)
    'uz līnijas'
    >>> check_coordinates(4,8)
    'ārpuss'
    >>> check_coordinates(-4,1)
    'ārpuss'
    >>> check_coordinates(3,2)
    'iekšā'
    """
    funk=round(-(6/4.2)*punkts_x+13.714, 3)
    funk2 = round(12*punkts_x+38, 3)
    if punkts_x>=-3 and punkts_x<= 8.2 and punkts_y>=2 and  punkts_y<= 8 and  punkts_y<=funk and  punkts_y<=funk2:
        if punkts_y==2 or punkts_y==8 or punkts_y==funk or punkts_y==funk2:
            print('uz līnijas')
        else:
            print('iekšā')
    else:
        print('ārpuss')        
   

   
doctest.testmod(verbose=True)

punkts_x = float(input("Ievadiet x Koordināti: "))
punkts_y = float(input("Ievadiet y Koordināti: "))

check_coordinates(punkts_x, punkts_y)