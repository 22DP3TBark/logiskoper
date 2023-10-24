x = int(input("X: "))
y = int(input("y: "))

if x>-5 and x<2 and y >-1 and y<3:
    print("ieksa")
elif x == -5 or x == 2 and y>= -1 and y <= 3:
    print("uz robež līnijas ")
else:
    print("Ārpus")        