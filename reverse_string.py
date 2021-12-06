def reverse(s):

    str= ''
    k= len(s)
    while k > 0:
        str += s[ k- 1 ]
        k = k - 1
    return str
print(reverse('shabeena'))