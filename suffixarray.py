INPUT = "taastaataaasdfaskdjfgkaewvfasfcztawdrfjhawegrfasxcvfjsadfkjegrftkjedgfikdsuxvfksdgha"

def suffixArray(text):
    n = len(text)
    text += "\0\0\0"
    n0 = (n+2) / 3
    n1 = (n+1)/3
    n2 = n/3

    print("n=n0+n1+n2")
    print(str(n) + "=" + str(n0+n1+n2)  + "=" + str(n0) + "+" + str(n1) + "+" + str(n2))
    print("")

    s12 = []
    for i in range(0,n):
        if not i % 3 == 0:
            s12.append(i)
    
    for i in range(0,n1+n2-1):
        for j in range(0,n1+n2-1-i):
            l = s12[j]
            r = s12[j+1]
            if lexiGT(text[l], text[l+1],text[l+2], text[r], text[r+1],text[r+2]):
                tmp = s12[j]
                s12[j] = s12[j+1]
                s12[j+1] = tmp

    # s12 is now sorted by the triples they represent
    print("SA12")
    for i in s12:
        print(str(i) + ":\t" + str(text[i:-3]))
    print("")

    names = [1]*(n1+n2)
    name = 1
    if s12[0] % 3 == 1:
        nameindex = s12[0]/3
    else:
        nameindex = n1 + s12[0]/3

    names[nameindex] = 1

    for i in range(1,n1+n2):
        l = s12[i-1]
        r = s12[i]
        
        if lexiGT(text[r], text[r+1],text[r+2], text[l], text[l+1],text[l+2]):
            name += 1

        if r % 3 == 1:
            nameindex = r/3
        else:
            nameindex = n1 + r/3

        names[nameindex] = name
        print(str(nameindex) + ":" + str(name))
    print("names")
    for i in range(0,len(names)):
        print(str(names[i]))
    print("")   

    if name < n1+n2:
        print("duplicates, need to dig deeper")
        print("-----recursion down--------\n")
        name_suffix_array = suffixArray(names)
        print("\n----recursion up-----------\n")
        name = 1
        for i in range(0,n1+n2):
            names[name_suffix_array[i]] = name
            name += 1

        print("names after recursion")
        for i in range(0,len(names)):
            print(str(names[i]))
        print("")
   # unique names found for s12

    #if the last index is mod 3 == 0 then for the merge we need a dummy name for the "next" suffix
    names += [0]

    # sort s0
    s0 = []
    for i in range(0,n0):
        s0.append(i*3)

    for i in range(0,n0):
        for j in range(0, n0-1-i):
            l = s0[j]
            r = s0[j+1]
            if text[l] > text[r] or (text[l] == text[r] and names[l/3] > names[r/3]):
                tmp = s0[j]
                s0[j] = s0[j+1]
                s0[j+1] = tmp
    
    print("SA0")
    for i in s0:
        print(str(i) + ":\t" + str(text[i:-3]))
    print("")


    count12 = 0
    count0 = 0
    result = []

    while count0 < n0 and count12 < n1+n2:
        i12 = s12[count12]
        i0 = s0[count0]
        if i12 % 3 == 1:
            if text[i0] > text[i12] or (text[i0] == text[i12] and names[i0/3] > names[count12]):
                result.append(i12)
                count12 += 1 
            else:
                result.append(i0)
                count0 += 1
        else:
            if lexiGT(text[i0], text[i0+1], names[n1+(i0/3)], text[i12], text[i12+1], names[count12]):
                result.append(i12)
                count12 += 1
            else:
                result.append(i0)
                count0 += 1
    for i in range(count0,n0):
        result.append(s0[i])

    for i in range(count12,n1+n2):
        result.append(s12[i])

    text = text [:-3]

    print("SA")
    for i in result:
        print(str(i) + ":\t" + str(text[i:]))

    return result
def lexiGT(a1,a2,a3,b1,b2,b3):
    res = a1 > b1 or (a1 == b1 and a2 > b2) or (a1 == b1 and a2 == b2 and a3 > b3)
    return res

suffixArray(INPUT)
