if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    mylst = [x for x in range(x + 1)]
    print(mylst)
    jlst = [x for x in range(y + 1)]
    print(jlst)
    k = [x for x in range(z + 1)]
    print(k)

    newlst=[0,0,0]
    mainlst=[]
    mainlst.append(newlst)
    for x in range(x+1):
        newlst.insert(0,x)
        for y in range(y+1):
            newlst.insert(1,x)
            for z in range(z + 1):
                newlst.insert(2,z)
                # print(newlst)
                mainlst.__add__(newlst)



    print(mainlst)
    finallst=mainlst[0]
    finallst.reverse()
    print(finallst)