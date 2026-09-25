def elementlar(sonlar):
    ikkilanga = []
    a = 2
    for i in sonlar:
        i = i * a
        ikkilanga.append(i)

    return ikkilanga

sonlar = [1,2,3]
natija = elementlar(sonlar)

print(natija)
# ishladi 