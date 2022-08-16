kun = input("Bugun qaysi kun?  ")
harorat = float(input("Havo harorati qanday? "))
if (kun.lower()== 'shanba' or kun.lower()== 'yakshanba') and harorat>=30:
    print("Cho`milishga kettik. ")
elif (kun.lower()== 'shanba' or kun.lower()== 'yakshanba') and harorat<30:
    print("Uyda dam olamiz.")
else : print('Bugun ish kuni')