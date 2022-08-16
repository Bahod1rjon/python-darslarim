


kod = int(input("Maxsulot kodini kiriting: .... >>  "))
kurs = int(input("O'zgaruvchan summani kiriting: >>  "))
k_summa=kod*kurs//0.75
o_tolov = int(input("Oldindan to`lov miqdorini kiriting: .. >>  "))
print("Mahsulotni muddatli to`lov uchun narhi >> ",k_summa,"\n")
print("4 oy muddatga har oy", (k_summa-o_tolov)//4 , "so`mdan to`lab borasiz:\n")
print("6 oy muddatga har oy", (k_summa-o_tolov)*1.18//6 , "so`mdan to`lab borasiz:\n")
print("12 oy muddatga har oy", (k_summa-o_tolov)*1.36//12 , "so`mdan to`lab borasiz:\n")
print("Tashrifingiz uchun rahmat\n")
