import random
import string
len = int(input("ENTER THE PASSWORD LENGTH YOU NEED: "))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbol = string.punctuation
lp = lower
up = upper
np = num
sp = symbol
lup = lower + upper
lnp = lower + num
lsp = lower + symbol
unp = upper + num
usp = upper + symbol
nsp = num + symbol
lunsp = lower + upper + symbol + num

print('''How does your password show?
        1.only lower case
        2.only upper case
        3.only numbers
        4.only symbols
        5.lower + upper
        6.lower + number
        7.lower + symbol
        8.upper + number
        9.upper + symbol
        10.number + symbol
        11.lower + number + upper + symbol''')


enter = int(input("ENTER: "))

if enter == 1:
    rp1 =random.sample(lp,len)
    rp1 = "".join(rp1)
    print(rp1)
elif enter == 2:
    rp2 = random.sample(up,len)
    rp2 = "".join(rp2)
    print(rp2)
elif enter == 3:
    rp3 =random.sample(lp,len)
    rp3 = "".join(rp3)
    print(rp3)
elif enter == 4:
    rp4 =random.sample(sp,len)
    rp4 = "".join(rp4)
    print(rp4)
elif enter == 5:
    rp5 =random.sample(lup,len)
    rpl = "".join(rp5)
    print(rp5)
elif enter == 6:
    rp6 =random.sample(lnp,len)
    rp6 = "".join(rp6)
    print(rp6)
elif enter == 7:
    rp7 =random.sample(lsp,len)
    rp7 = "".join(rp7)
    print(rp7)
elif enter == 8:
    rp8 =random.sample(unp,len)
    rp8 = "".join(rp8)
    print(rp8)
elif enter == 9:
    rp9 =random.sample(usp,len)
    rp9 = "".join(rp9)
    print(rp9)
elif enter == 10:
    rp10 =random.sample(nsp,len)
    rp10 = "".join(rp10)
    print(rp10)
elif enter == 11:
    rp11 =random.sample(lunsp,len)
    rp11 = "".join(rp11)
    print(rp11)






    








            











        
