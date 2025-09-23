import os
os.system("cls")

bekertSzam = int(input("Adj meg egy számot: "))

for x in range(0,bekertSzam+1):
    if x%4==0:
        print(x)