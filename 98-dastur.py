maxsulotlar = ['kirmoshina','pelisos','televizor','haladelnik','ventilator','gaz','pech','termos','tifal','tog\'ara']
savat = []
print('Siz oladigan 5ta maxsulot turini kiriting;')
for n in range(5):
    savat.append(input(f"{n+1} "))
for maxsulot in savat:
    if maxsulot in maxsulotlar:
        print(f"{maxsulot} do\'konimizda bor.".title())
    else :
        print(f"{maxsulot} do\'konimizda yo\'q.")
