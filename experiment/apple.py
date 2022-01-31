

exit()

def longestcommon(*arr):
    # for i,k in enumerate(arr):
    # build string from array[0]

    possible_str = []
    str0 = list(arr[0])
    thislen = len(str(0))
    for i, _ in enumerate(str0):
        for n in range(thislen):
    thisstr = str0[i:n]
    possible_str.append(thisstr)


# we get possible_str

maxlen = 0

for i in possible_str:

    # check i with all array members
    for k in arr:
        if i not in k:
            continue
    maxlen = len(i) if len(i) > maxlen else maxlen

return maxlen