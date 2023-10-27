"""
autors: teodors
Programma pārbauda punkta koordinates figurai. rinķim, riņķa centrs atrodas punkta 0,0 rinķa radius 1 vienība

"""

def parbaudit_punkta_koordinates(punkta_x,punkta_y: float) -> int:
    import math
    if math.sqrt(punkta_x**2+punkta_y**2) <= 1:
        if math.sqrt(punkta_x**2+punkta_y**2) == 1:
            return 2
        else:
            return 1
    else:
        return 3    

parbaudit_punkta_koordinates(0.6, 0.8)
