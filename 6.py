def qiymatlar_yigindis(dictt_malumotlari):
    yigindi = 0
    for i,j in dictt_malumotlari.items():

        yigindi += j
    return yigindi

malumotlar = {"a":1,"b":2,"c":3}
natija = qiymatlar_yigindis(malumotlar)

print(natija)

# ishladi 