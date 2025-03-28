import math
def caeser():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string = input("enter a string").lower()
    change = int(input('How much do you want to change it by'))
    newstring = ''
    for i in string:
        count = 0
        if i in alphabet:
            for a in alphabet:
                if a != i:
                    pass
                else:
                    break
                count = count + 1
            if len(alphabet)-count < count+change:
                newstring = newstring + alphabet[(count+change) % len(alphabet)]
            else:
                newstring = newstring + alphabet[count+change]
        else:
            newstring = newstring + i
    print(newstring)
    
def affine():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string = input('enter some text')
    b = int(input('What do you want the intercept to be'))
    newstringvalues = []
    newstring = ''
    for i in string:
        if i in alphabet:
            count = 0
            for a in alphabet:
                if a == i:
                    break
                else:
                    count = count + 1
            newvalue = ((17*(count+1))+b) % 26
            newstringvalues.append(newvalue)
        else:
            newstringvalues.append(i)
    
    print(newstringvalues)
    for i in newstringvalues:
        if isinstance(i, int) == True:
            newstring = newstring + alphabet[i-1]
        else:
            newstring = newstring + i
    print(newstring)
    
def vigenere():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string = input('enter some text').lower()
    key = input('Enter the key word (only letters, sometimes works)').lower()
    fullkey = ''
    listkey = []
    newstring = ''
    times = len(string)/len(key)
    for i in range(math.floor(times)):
        fullkey = key * math.floor(times)
    fullkey = fullkey + key[:int(len(key)/2)]
    for i in fullkey:
        count = 0
        for a in alphabet:
            if a != i:
                count = count + 1
            else:
                break
        listkey.append(count)
    iterationcount = 0
    for i in string:
        count = 0
        if i in alphabet:
            for a in alphabet:
                if a != i:
                    pass
                else:
                    break
                count = count + 1
            if (len(alphabet)-count) < count + listkey[iterationcount]:
                newstring = newstring + alphabet[(count+listkey[iterationcount]) % len(alphabet)]
            else:
                newstring = newstring + alphabet[count + listkey[iterationcount]]
            iterationcount = iterationcount + 1
        else:
            newstring = newstring + i
    print(newstring)   
