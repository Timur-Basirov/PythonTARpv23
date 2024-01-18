print("Hello world!")
#1
try:
    name=input("What is your name?") #name это что-то как группа чтобы данные были разделены.
    age=int(input("How old are you?")) #вторая группа #float()->2.5
    print("Welcome! "+name+". You are"+str(age)+" years old") #При помощи str код воспринимает input age как текст и дает возможность его приклеить к другому str формату.
    print("Welcome!",name,". You are",age,"years old")
    print("Welcome! {0} You are {1} years old!".format(name,age)) #.format (x0,x1,x2,x3) и так далее комбинируется вместе с {}
    print("Muutuja age=",age,",tüüp on",type(age))
except:
    print("Viga andmetüübiga")
print()

#2
vanus=18
eesnimi="Jaak"
pikkus=16.5
kas_käib_koolis=True
print()

print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_käib_koolis))
print()

#3
from random import *
kokku=randint(10,100)
print("Kokku",kokku)
try:
    mitu=int(input("Mitu kommi tahad võtta?"))
    kokku-=mitu
    print("Nüüd Laua peal on",kokku,"kommid")
except:
    print("Viga andmetüübiga")
print()

#4
import math
try:
    print("Tere, ma aitan teil arvutada puu läbimõõtu!")
    c=(float(input("Kui pikk on teie puu ümbermõõt?")))
    d=c/math.pi
    print("Teie puu läbimõõt on", d)
except:
    print("Viga andmetüübiga")
print ()

#5
import math
try:
    print("Tere, ma aitan teil arvutada krundi diagonaali pikkust!")
    N=(float(input("meetri pikkune")))
    M=(float(input("meetri laiune")))
    D=math.sqrt(N**2 + M**2)
    print("Krundi diagonaali pikkus on", D)
except:
    print("Viga andmetüübiga")
print()

from random import * 
#6
try:
    aeg=float(input("Mitu tundi kulus sõiduks? ")) #aeg ei saa olla 0
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
    kiirus = teepikkus/aeg 
    print("Sinu kiirus oli " + str(kiirus) + " km/h")
except :
    print("Viga andmetüübiga")
print()    
#7
try:
    
    n1=int(input("Sisestage esimene number:"))
    n2=int(input("Sisestage teine number:"))
    n3=int(input("Sisestage kolmas number:"))
    n4=int(input("Sisestage neljas number:"))
    n5=int(input("Sisestage viies number:"))
    avg=(n1+n2+n3+n4+n5)/5
    print("aritmeetiline keskmine on:", avg)
except :
    print("Viga andmetüübiga")
print()

#8
print("FROG!!!")
print("   @..@")
print("  (----)")
print(" ( \__/ )")
print("  ^^ "" ^^")
print()

#9
try:
    A=int(input("Küljepikkus A"))
    B=int(input("Küljepikkus B"))
    C=int(input("Küljepikkus C"))
    perimeter=A+B+C
    print("perimeter on", perimeter)
except:
    print("Viga andmetüübiga")
print()

#10
from random import *
P=randint(1,5)
price=12.90
price*=1.1 #price + tips
osa=round(price/P,2)
print("Each friend paid: ",osa)

