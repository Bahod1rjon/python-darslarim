maxsulotlar = ['un','yog\'','olma','nok','non','uzum']
savat =[]
for n in range(5):
    savat.append(input(f"Savatga {n+1} maxsuotni qo`shing:"))
bor_maxsulotlar = []
yoq_maxsulotlar = []
for maxsulot in savat:
    if maxsulot in maxsulotlar:
        bor_maxsulotlar.append(maxsulot)
    else: yoq_maxsulotlar.append(maxsulot)
if yoq_maxsulotlar:
    print(f"Do`konimizda quyidagi maxsulotlar yo`q.")
    for maxsulot in yoq_maxsulotlar:
        print(maxsulot)
else : print("Siz so`ragan barcha maxsulot do`konimizda bor.")