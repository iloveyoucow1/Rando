"""Doc String"""

STRING_ONE = "abcabcbb"

def longest_sub_string(string):
    """doc string"""


    string = list(string)
    tmp = ""
    tmparr = []

    for i in string:

        if tmparr is not None:
            for x in tmparr :
                if i != x :
                    tmp = tmp + i
                    tmparr += i
                    print(tmparr)
                if i == x :
                    break
        if tmp == "":
            tmp = i
            tmparr = [i]



    return tmp

print(longest_sub_string(STRING_ONE))
