def eliLR(a):
    S = []
    Sd = []
    t = 0
    temp = list(a[3:].split('|'))
    for p in temp:
        if a[0]!=p[0]:
            continue
        else:
            t = 1
    if t==0:
        print("No Left Recursion")
        return
    elif t==1:
        for p in temp:
            if a[0] == p[0]:
                Sd.append(p[1:])
            else:
                S.append(p)
        st1 = ""
        for i in list(set(S)):
            st1 += "{}{}'|".format(i,a[0])
        st2 = ""
        for i in Sd:
            st2 += "{}{}'|".format(i,a[0])
        st2 += "Epsilon"

        print("{}->{}".format(a[0], st1[:-1]))
        print("{}'->{}".format(a[0], st2))


g = []
n = int(input("No.of Productions : "))
for i in range(n):
    pst = ""
    l = input("Enter LHS-{} : ".format(i + 1))
    pst = l + "->"
    k = int(input("Enter number of RHS productions : "))
    temp1 = ""
    for j in range(k):
        r = input("Enter RHS-{} : ".format(j + 1))
        temp1 += "{}|".format(r)
    pst += temp1[:-1]
    g.append(pst)
print("\n---Grammer---")
for i in range(len(g)):
    print(g[i])
print("\n---After Elimination of Left Recursion---")
for i in range(len(g)):
    eliLR(g[i])
