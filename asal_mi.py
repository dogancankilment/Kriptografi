import math

a=input("Kontrol sayisini giriniz\n")

def asal_kontrol(a):
        y = math.sqrt(a) #karekok
        if y == 1: # her sefer kontrol ediyor
                return 1
        for i in range(2,int(y)+1):
                if asal_kontrol(i): # recursive
                        if not (a%i):
                                return 0 #asal degil
        return 1

if ( asal_kontrol(a) ):
        print "sayi asaldir"
else:
        print "sayi asal degildir"

