def convert_pig_latin(text):
    orglist = text.split()
    finallist = []
    for i in range (len(orglist)):
        templist = [x for x in orglist[i]]
        if templist[0] in 'aeiouy':
            templist.append('yay')
            tempstr = ''.join(templist)
            finallist.append(tempstr)
        else:
            while templist[0] not in 'aeiouy':
                tempchar = templist[0]
                templist.pop(0)
                templist.append(tempchar)
            templist.append('ay')
            tempstr = ''.join(templist)
            finallist.append(tempstr)
    finalstr = " ".join(finallist)
    return finalstr
