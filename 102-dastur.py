son = int(input("Butun sonni kiriting:   "))
for n in range(2,11):
    if not (son % n) :
        print(f"{son} {n} ga qoldiqsiz bo`linadi")
#print(son)