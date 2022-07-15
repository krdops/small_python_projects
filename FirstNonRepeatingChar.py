


def nonrepeat(stringx):
    count = 0
    for i in stringx:

            if stringx[count] != stringx[count+1] and stringx[count] != stringx[count-1]:
                return stringx[count]

            count += 1


stringx = 'aaaadddeerrrrrrrfffffgghhbbbbbbbbbbbbbbbbbbt'
print(nonrepeat(stringx))
