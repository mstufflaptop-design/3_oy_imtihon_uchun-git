def musbatga_olib_otish(sonlar):
    musbatlar = []
    a = -1
    for i in sonlar:
        if i<0:
            i= i*a
            musbatlar.append(i)
        else:
            musbatlar.append(i)
    return musbatlar

sonlar = [-3,2,-1]
natija = musbatga_olib_otish(sonlar)

print(natija)
# ishladi