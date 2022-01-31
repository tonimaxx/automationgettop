import string
# https://docs.python.org/3/library/string.html

# List to Dict
# key1 = ["<div>", "<p>", "<b>"]
# key2 = ["</div>", "</p>", "</b>"]
# new_dict = {key1: key2 for key1, key2 in zip(key1, key2)}
# print(new_dict)

def is_palindrome(*args):
    return True if args == args[::-1] else False

def is_duplicate(x):
    a = {c: x.count(c) for c in set(x)}
    maxvalue = max(a.values())
    return True if maxvalue > 1 else False

def is_anagram(x,y):
    # Count char in string
    a = {c: x.count(c) for c in set(x)}
    b = {c: y.count(c) for c in set(y)}
    # Remove " " from Dict
    if " " in a: a.pop(" ")
    if " " in b: b.pop(" ")
    # print(a,b)
    return True if a == b else False

def string_tag_count(str):
    # Example Str
    # str = "<div><div><div><p></p></div></b>"

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

print(string_tag_count("<div><div><div><p></p></div></b></b></b>"))



# print(is_duplicate("abcdef"))

exit()


print(is_palindrome("madam"))
print(is_anagram("aacabb","bbaaac"))
print(is_anagram("schoolmaster","the class rooms"))
print(is_anagram("the Morse Code", "here Come dots"))

# Palindrome-inator: Given a string, check if characters of the given string can be rearranged to form a palindrome. If a palindrome is possible, return a True otherwise return False.

# palindrome(“aabb”) => True
# palindrome(“tacos”) => False

# https://app.coderpad.io/FG63T3HM
def palindrome(x):
    a = {c: x.count(c) for c in set(x)}
    b = list(a.values())
    d = {c: b.count(c) for c in set(b)}
    if not 1 in d: return True
    return True if d[1] == 1 else False

# ------------------------------
def is_part_of_string(a_string,matches):
    if any(a := [x in a_string for x in matches]):
            return (True)
    else: return False

a_string = "A string is more than its parts!"
matches = ["more", "wholesome", "milk"]
print(is_part_of_string(a_string,matches))
# ------------------------------





# Program to show various ways to read and
# write data in a file.
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes

file1 = open("myfile.txt", "r+")

print("Output of Read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth
# bite from the beginning.
file1.seek(0)

print("Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)

# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()

file1.seek(0)

print("Output of Readline(9) function is ")
print(file1.readline(9))

file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()



# CSV

import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')