import string

def string_tag_count(str):


    str = "<div><div><div><p></p></div></b>"

    key1 = ["<div>", "<p>", "<b>"]
    key2 = ["</div>", "</p>", "</b>"]

    keycount1 = [str.count(key) for key in key1]
    keycount2 = [str.count(key) for key in key2]
    print(keycount1)
    print(keycount2)

    keycount_dif = list(map(lambda x,y:x-y, keycount1, keycount2))
    print(keycount_dif)

    result = []
    for i,j in enumerate(keycount_dif):
        if j > 0:
            result.append(f"{key1[i]} has {j} more")
        elif j == 0:
            result.append(f"{key1[i]} & {key2[i]} are equal")
        elif j < 0:
            result.append(f"{key2[i]} has {abs(j)} more")

    return (", ".join(result))

print(string_tag_count("<div><div><div><p></p></div></b>"))

