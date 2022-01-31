def xhandler(key, is_caps=False, is_shift=False):
    print(key, is_caps, is_shift)
    if not isinstance(key, str): return "KeyError"
    if len(key) != 1: return "KeyError"
    if key.isalpha() and key.isupper(): return "KeyError"
    if key.isalpha() and (is_caps or is_shift):
        if is_caps and is_shift: return key.lower()
        return key.upper()
    upperkeys = '!@#$%^&*()_+{}:<>?"|~'
    lowerkeys = '1234567890-=[];,./\'\\`'
    table = key.maketrans(lowerkeys, upperkeys)
    if is_shift: return key.translate(table)
    if key.isdigit(): return key
    return key

def handler(key, is_caps=False, is_shift=False):
    if not isinstance(key, str) or len(key) != 1 or (key.isalpha() and key.isupper()) : return "KeyError"
    if key.isalpha() : return key.upper() if is_caps != is_shift else key.lower()
    upperkeys,lowerkeys = '!@#$%^&*()_+{}:<>?"|~','1234567890-=[];,./\'\\`'
    # table = key.maketrans(lowerkeys, upperkeys)
    if is_shift: return key.translate(key.maketrans(lowerkeys, upperkeys))
    if key.isdigit(): return key
    return key

print(handler('a', False, False))

exit()

def palindromable(a):
    # print(set(a))
    b = {i: a.count(i) for i in set(a)}
    c = [i for i in b.values() if not i%2]
    return False if len(c) > 1 else True

# print(palindromable("aa"))

