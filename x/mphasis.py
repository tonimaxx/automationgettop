str1 = "state"
str2 = "taste"

def is_anagram(str1, str2):
    charcount1 = {}
    for i,j in enumerate(str1):
        if j in charcount1:
            charcount1[j] = charcount1[j] + 1
        else:
            charcount1[j] = 1
    charcount2 = {}
    for i,j in enumerate(str2):
        if j in charcount2:
            charcount2[j] = charcount2[j] + 1
        else:
            charcount2[j] = 1

    for i,j in enumerate(charcount1):

        # print(charcount1[j])
        try:
            if charcount1[j] != charcount2[j]:
                return False
        except:
            return False

    return True


    # return charcount1, charcount2

print(is_anagram("state","taste"))
print(is_anagram("hello","world"))
print(is_anagram("hello","olleh"))
print(is_anagram("hello","ollehh"))
print(is_anagram("hello","olehh"))



