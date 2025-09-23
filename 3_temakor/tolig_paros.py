import os
os.system("cls")

tol = int(input("Adj meg a kezdő számot: "))
ig = int(input("Adj meg vég számot: "))
for x in range(tol,ig+1):
    if x%2==0:
        print(x)