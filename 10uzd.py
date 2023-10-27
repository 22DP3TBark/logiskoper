"""
autors: teodors
Programma pārbauda punkta koordinates figurai. rinķim, riņķa centrs atrodas punkta 0,0 rinķa radius 1 vienība



"""
import doctest

def parbaudit_punkta_koordinates(punkta_x,punkta_y: float) -> int:
    """
    Funkcija pārbauda punkta koordinates (punkta_x; punkta_y) figūrai rinķim, rinķa centrs atrodas punkta 0, 0, rinķa radius 1 vieniba.

    parameters 
    -----------
    punkta_x : float
        punkta x koordinate Dekartu plakne.
     punkta_y : float
        punkta x koordinate Dekartu plakne. 

    returns
    --------------
    int 
       1 - iekšā, 2 - uz līnijas, 3 - ārpuss

    >>> parbaudit_punkta_koordinates(1,1)
    3
    >>> parbaudit_punkta_koordinates(-0.6,1.2)
    3
    >>> parbaudit_punkta_koordinates(0,1)
    2
    >>> parbaudit_punkta_koordinates(-1,0)
    2
    >>> parbaudit_punkta_koordinates(0,1)
    2
    >>> parbaudit_punkta_koordinates(1,0)
    2
    >>> parbaudit_punkta_koordinates(0.5,0.5)
    1
    >>> parbaudit_punkta_koordinates(-0.3,0)
    1
    >>> parbaudit_punkta_koordinates(0,0)
    1
    >>> parbaudit_punkta_koordinates(0.6,0.8)
    2

    """
    import math
    if math.sqrt(punkta_x**2+punkta_y**2) <= 1:
        if math.sqrt(punkta_x**2+punkta_y**2) == 1:
            return 2
        else:
            return 1
    else:
        return 3    

doctest.testmod(verbose=True)
