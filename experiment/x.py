import collections


def lowest(s):
    a = [s.count(c) for c in set(s)]
    odd = [x for x in a if x % 2 != 0]
    even = [x for x in a if x % 2 == 0]
    unique_even = [x for x in set(even)]
    member_even = len(unique_even)
    member_odd = len(odd)
    print(s)
    print(f"u = {sum(unique_even)}")
    print(f"mueven = {member_even}")
    print(f"modd = {member_odd}")
    # c = len(a) - len(b)
    print(odd)
    print(even)

    if len(odd) == 0 : return sum(even)
    return 1 if len(odd) > len(even) else sum(unique_even) + 1
    # print(f"c = {c}")
    # print(len(b))


    # print(b)
    # return 1

print(lowest("aabbccdd"))
# print(lowest("aebecda"))
# print(lowest("eutxutuatgextu"))
# print(lowest("abbddc"))
# print(lowest("aebecdaa"))
# print(lowest("abcddcba"))
# print(lowest("abcd"))

exit()


str = "the quick brown fox jumps over a lazy dog"
search = ['quick','quick brown', 'lazy','cat']

b = {b:str.find(b) for b in search}
print(b)

b.pop("quick")
print(b)

c = {x:str.count(x) for x in set(str)}

d = dict(sorted(c.items()))
print(d)

print(sorted(c.items(),key = lambda x:x[1]))



exit()
def past(h, m, s):
    return h*36*10**5+m*6*10**4+s*10**3

print(past(1,1,1))



exit()

def xunique_in_order(iterable):
    # a = list(iterable)
    latestchar = ""
    toreturn = []
    for i,n in enumerate(list(iterable)):
        if n != latestchar:
            toreturn.append(n)
            latestchar = n
    return toreturn

# from itertools import groupby

def unique_in_order(iterable):
    return [n for (n,_) in __import__('itertools').groupby(iterable)]



print(unique_in_order('AAAABBBCCDAABBB'))