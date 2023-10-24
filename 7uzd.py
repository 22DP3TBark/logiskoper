x = int(input("X: "))
y = int(input("y: "))

if x > -1 and x < 3 and y > -2 and y < 1:
    print("ieksa")
elif x == -1 or x == 3 and y>= -2 and y <= 1:
    print("uz robež līnijas ")
else:
    print("Ārpus")        