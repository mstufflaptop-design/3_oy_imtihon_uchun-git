def musbat_sonlar(sonlar):
    sum = 1
    for x in sonlar:
        if x>0:
            sum= sum*x
    return sum


sonlar =[1,2,3,4]
natija = musbat_sonlar(sonlar)

print(natija)
# ishladi !