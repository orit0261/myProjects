string = list('The quick brown fox jusmps over the lazy dog')
result = []
for i in string:
        if i == 'o':
                i = '0'
        result.append(i)
print(''.join(result))