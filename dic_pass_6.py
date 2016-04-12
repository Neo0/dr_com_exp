import os

pds=[]


rg=range(0,10)

for first in rg:
    for second in rg:
        for three in rg:
            for four in rg:
                for five in rg:
                    for six in rg:
                        num= "%s%s%s%s%s%s"%(first,second,three,four,five,six)
                        pds.append(num)



file_object = open('pwdNum6.txt', 'w')
file_object.writelines(['%s%s' % (x,os.linesep) for x in pds])
file_object.close( )
