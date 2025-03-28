import cyphers

cyphers = ['caeser','affine', 'vigenere']
print('Available cyphers:')
for i in cyphers:
    print(i)
cypher = input('enter one of the above cyphers').lower()
if cypher in cyphers:
    if cypher == 'caeser':
        cyphers.caeser()
    elif cypher == 'affine':
        cyphers.affine()
    elif cypher == 'vigenere':
        cyphers.vigenere()
