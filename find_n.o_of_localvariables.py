def find_localvar():
    x = 1
    y = 'hello'
    print('shabeena')

print(find_localvar.__code__.co_nlocals)