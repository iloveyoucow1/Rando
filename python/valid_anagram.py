#Valind Anagram Leet Code Solution Problem 242
s = "rat"
t = "car"

def valid(s, t):

    sarray = []
    tarray = []
    for i in s:
        sarray.append(i)
    for i in t:
        tarray.append(i)
    sarray.sort()
    tarray.sort()

    if sarray == tarray:
        return True
    else:
        return False

print(valid(s, t))