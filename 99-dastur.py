maxsulotlar = ['kirmoshina','pelisos','televizor','haladelnik','ventilator','gaz','pech','termos','tifal','tog\'ara']
savat = []
bor_maxsulotlar =[]
yoq_maxsulotlar =[]
print('Siz oladigan 5ta maxsulot turini kiriting;')
for n in range(5):
    savat.append(input(f"{n+1} "))
for maxsulot in savat:
    if maxsulot in maxsulotlar:
        print(f"{maxsulot} do\'konimizda bor.".title())
        bor_maxsulotlar.append(f"{maxsulot}")
        
    else :
        print(f"{maxsulot} do\'konimizda yo\'q.")
        yoq_maxsulotlar.append(f"{maxsulot}")


#print(maxsulot, "Do\'konimizda bor.")
a = len(yoq_maxsulotlar)
if a==0:
   print("Siz so`ragan barcha maxsulotlar do`konimizda bor." )  
else : 
    print("Quyidagi maxsulotlar: ", yoq_maxsulotlar, 'do\'konimizda yo\'q.')

