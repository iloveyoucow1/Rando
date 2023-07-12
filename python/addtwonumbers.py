l1 = [2,4,3]
l2 = [5,6,4]

def addTwoNumbers(l1, l2):
    def reverse_list(arr):
        left = 0
        right = len(arr)-1
        while (left < right):
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1
        return arr
    l1 = reverse_list(l1)
    l2 = reverse_list(l2)
    tmpl1 = ""
    tmpl2 = ""

    for i in l1:
        tmpl1 += str(i)
    for i in l2:
        tmpl2 += str(i)
    
    tmp = int(tmpl1) + int(tmpl2)

    anwser = [int(x) for x in str(tmp) ]
    return anwser


print(addTwoNumbers(l1, l2))