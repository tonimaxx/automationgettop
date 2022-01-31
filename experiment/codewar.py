def xremove(s):
    char = ''
    foundchar = False
    for i in s[::-1]:
        if not foundchar:
            if i != '!':
                foundchar = True
                char = char+i
        else: char = char+i
    return char[::-1]


def remove(s):
    return s.rstrip('!')

    # return __import__("re").split("!+$",s)[0]

# print(remove('hi!'))
# print(remove('!hi!!!!'))

# print("toniMaxx".casefold()=="toniMAXX".casefold())
# print(list("tonimaxx")[::-1])

def xchristmas_tree(level):

    floor = []
    for i in range(1,level+1):
        star = ''
        for n in range(i*2-1):
            star = star.__add__("*")

        floor.append(star.center(level*2-1," "))
        print(floor[i-1])
    return floor

def christmas_tree(l):

    # r = ''
    # for i in range(1,level+1): r=r+('*'*(i*2-1)).center(level*2-1," ")+"\n"
    return ("\n".join([('*'*(i*2-1)).center(l*2-1) for i in range(1,l+1)]))
    # return r.rstrip("\n")
    # return r


# print(christmas_tree(5))

# ___*___
# __***__
# _*****_
# *******
#
# 1
# 3
# 5
# 7

def to_nato(words):
    # natostr = "Alfa,Bravo,Charlie,Delta,Echo,Foxtrot,Golf,Hotel,India,Juliett,Kilo,Lima,Mike,November,Oscar,Papa,Quebec,Romeo,Sierra,Tango,Uniform,Victor,Whiskey,Xray,Yankee,Zulu"

    nato = {chr(i+97):a.capitalize() for i, a in enumerate("Alfa,Bravo,Charlie,Delta,Echo,Foxtrot,Golf,Hotel,India,Juliett,Kilo,Lima,Mike,November,Oscar,Papa,Quebec,Romeo,Sierra,Tango,Uniform,Victor,Whiskey,Xray,Yankee,Zulu".split(','))}
    r = ''
    for i in words.lower():
        if i in nato: r = r+nato[i]+" "
        elif i in ",.!?": r = r+i+" "
    # return r.rstrip()


# print(to_nato('If you can read'))

def wrap(height, width, length):
    l = sorted([height,width,length])
    return (l[0]*4+l[1]*2+l[2]*2)+20

# print(wrap(17,32,11))

def toni(*args):
    print(args.count("t"))

toni("t","t","m")