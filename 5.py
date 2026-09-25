def manfiy_sonlar(sonlar):
    manfiylar = []
    for i in sonlar:
        if i <0:
            manfiylar.append(i)

    return manfiylar
sonlar = [3,-1,0,-7]
natija = manfiy_sonlar(sonlar)

print(natija)
# ishladi 