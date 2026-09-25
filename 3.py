def raqamlar_olish(matin):
    sonlar = "1234567890"
    natija = 0
    for i in matin:
        if i in sonlar:
          natija +=1
    return natija

sonlar = "abs123"
natija  = raqamlar_olish(sonlar)

print(natija)

# ishladi !