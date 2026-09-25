
def zerodivision(a,b):
    try:
        ab = a/b
    except zerodivision:
        matin = "Nolga bolish mumkun emas !"
    return matin

a = 10
b = 0

natija = zerodivision(a,b)
print(natija)

# ishladi 
