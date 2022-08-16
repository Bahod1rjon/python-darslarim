menu = ['osh','sho\'rva ','somsa','manti','lagmon']
buyurtmalar = []
if buyurtmalar:
    for taom in buyurtmalar :
        if taom in menu: 
            print(f"Menuda {taom} bor.")
        else : print(f"Kechirasiz menuda {taom} yo\'q.")
else: print('Savatingiz bo\'sh.')