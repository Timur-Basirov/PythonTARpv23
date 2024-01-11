#print("Hello world!")
#name=input("What is your name?") #name это что-то как группа чтобы данные были разделены.
#age=int(input("How old are you?")) #вторая группа #float()->2.5
#print("Welcome! "+name+". You are"+str(age)+" years old") #При помощи str код воспринимает input age как текст и дает возможность его приклеить к другому str формату.
#print("Welcome!",name,". You are",age,"years old")
#print("Welcome! {0} You are {1} years old!".format(name,age)) #.format (x0,x1,x2,x3) и так далее комбинируется вместе с {}
#print("Muutuja age=",age,",tüüp on",type(age))

#vanus=18
#eesnimi="Jaak"
#pikkus=16.5
#kas_käib_koolis=True 

#print(type(vanus))
#print(type(eesnimi))
#print(type(pikkus))
#print(type(kas_käib_koolis))

#from random import *
#kokku=randint(10,100)
#print("Kokku",kokku)
#mitu=int(input("Mitu kommi tahad võtta?"))
#kokku-=mitu
#print("Nüüd Laua peal on",kokku,"kommid")

#from random import *
##10
#P=randint(1,5)
#price=12.90
#price*=1.1 #price + tips
#osa=round(price/P,2)
#print("Each friend paid: ",osa)

from random import * 
#6
try:
    aeg=float(input("Mitu tundi kulus sõiduks? ")) #aeg ei saa olla 0
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
    kiirus = teepikkus/aeg 
    print("Sinu kiirus oli " + str(kiirus) + " km/h")
except :
    print("Viga andmetüübiga")
