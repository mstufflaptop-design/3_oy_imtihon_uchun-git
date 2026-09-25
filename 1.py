def musbat_sonlar(sonlar):
    natija = 0
    for son in sonlar:
        if son>0:
            natija += son

    return natija


sonlar =[1, -2, 3, -4, 5]
natija = musbat_sonlar(sonlar)

print(natija)

# ishladi !