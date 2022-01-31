def prime(n):
    to_return = []
    for i in range(n):
        j = i + 1
        # print()
        # print(f"j = {j}")
        for x in range(2,j):
            if x != j:
                # print(x,end=" ")
                if x%j != 0:
                    to_return.append(x)


    return set(to_return)

print(prime(10))

exit()
def greet():
    return __import__("base64").b64decode(b'aGVsbG8gd29ybGQh').decode('utf-8')


import base64

mystr = 'เมื่อไหร่จะจบเสียที .. Thailand Only'

# Encode
mystr_encoded = base64.b64encode(mystr.encode('utf-8'))
print(mystr_encoded)
# b'TyBKb8OjbyBtb3JkZXUgbyBjw6NvIQ=='

encoded = b'4LmA4Lih4Li34LmI4Lit4LmE4Lir4Lij4LmI4LiI4Liw4LiI4Lia4LmA4Liq4Li14Lii4LiX4Li1IC4uIFRoYWlsYW5kIE9ubHk='


mystr_encoded = base64.b64decode(encoded).decode('utf-8')
print(mystr_encoded)



greet()