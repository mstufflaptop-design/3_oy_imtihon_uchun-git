def factorial_sonlar(son):
    saqlandi =1
    for i in range(1,son,+1):
        saqlandi+=saqlandi*i
    return saqlandi

son = 5
natija = factorial_sonlar(son)

print(natija)

# ishladi 