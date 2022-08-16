from tkinter import Menu


menu = ['osh','shurva', 'manti','chuchvara','lag\'mon']
ovqat = input('Nima ovqat yeysiz?  >>> ')
if ovqat.lower() not in menu :
    print("Afsuskii bizda bunday taom yo`q.")
else: 
    print("Buyurtma qabul qilindi.")