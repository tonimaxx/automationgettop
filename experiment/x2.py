    a = """
                          /^--^\     /^--^\     /^--^\
                          \____/     \____/     \____/
                         /      \   /      \   /      \
                        |        | |        | |        |
                         \__  __/   \__  __/   \__  __/
    |^|^|^|^|^|^|^|^|^|^|^|^\ \^|^|^|^/ /^|^|^|^|^\ \^|^|^|^|^|^|^|^|^|^|^|^|
    | | | | | | | | | | | | |\ \| | |/ /| | | | | | \ \ | | | | | | | | | | |
    | | | | | | | | | | | | / / | | |\ \| | | | | |/ /| | | | | | | | | | | |
    | | | | | | | | | | | | \/| | | | \/| | | | | |\/ | | | | | | | | | | | |
    #u##r##y##y##b#############################################j##b##e##y##q#
    | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
    | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
    """
    b = list(a)
    s = ''.join(list(filter(lambda x:x.isalpha(),b)))
    print(s)
    a = len(s)
    s1 = slice(0,len(s)//2)
    s2 = slice(len(s)//2, len(s))
    print(s[s1], s[s2])
    # print(codecs.encode(a, 'rot_13'))
    # print(''.join(x))
    print(__import__("codecs").decode(f"{s[s1]} {s[s2]}!", 'rot_13'))


exit()

def filter_list(l):
    # x = filter(lambda x:type(x) is int,l)
    return list(filter(lambda x:type(x) is int,l))

print(filter_list([1,2,'a','b']))

exit()
def no_space(x):
    return ''.join((x.split()))


exit()
def find_needle(haystack):
    return f"found the needle at position {haystack.index('needle')}"

print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))

exit()

def order(sentence):
  x = [int(x)-1 for x in list(sentence) if x in '1234567890']
  a = dict(zip(x,sentence.split()))
  return " ".join([a[x] for x in range(len(a))])

print(order("4of Fo1r pe6ople g3ood th5e the2"))
