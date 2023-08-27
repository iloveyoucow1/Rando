strs = ["eat","tea","tan","ate","nat","bat"]

def group(strs):
    temp1 = []
    for i in strs:
        temp1.append(sorted(i))
    print(temp1)


print(group(strs))