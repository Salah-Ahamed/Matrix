#Defining GetValues() function
def GetValues(ms):
    global fl1
    global fl2
    fl1=[]
    fl2=[]
    r=int(ms[0])
    c=int(ms[2])
    rc=1
    cc=1
    while (rc<=r):
        print("\r")
        while(cc<=c):
            i=int(input("Value for ("+str(rc)+","+str(cc)+") : "))
            fl1.append(i)
            cc+=1
        fl2.append(fl1)
        fl1=[]
        cc=1
        rc+=1

#Defining DisMatrix() function
def DisMatrix():
    for i in (fl2):
        print("\r")
        for j in i:
            print(j,end=" ")

#Defining PrintNew(fl2) function
def PrintNew(mul):
    for i in fl2:
        print("\r")
        for j in i:
            print(j*mul,end=" ")

