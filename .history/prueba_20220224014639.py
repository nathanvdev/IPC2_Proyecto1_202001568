doc = 'WBWBWWWB'
ret = ''
for x in doc:
    print(x)
    if x == 'W':
        ret += '1'
    else:
        ret += '0'

print(ret)