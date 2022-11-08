op1,op2 = "",""
gam = ""
sizeofp = []
temp = input("Enter parent Non-Terminal : ")
gam += temp
op1 += gam + "\'->"
gam += "->"
op2 += gam
N = int(input("Enter no.of productions : "))
for i in range(N):
    p1 = input("Enter production {0} : ".format(i+1))
    sizeofp.append(len(p1))
    gam += p1
    if i!=N-1:
        gam += "|"
print(gam)
k = 3
l = []
for i in range(N):
    if gam[0] == gam[k]:
        l.append(1)
        print("Production {0} has left recursion".format(i + 1))
        if gam[k]!='#':
            for j in range(k+1,k+sizeofp[i]):
                op1 += gam[j]
            k = j+1
            op1 += gam[0]
            op1 += "\'|"
    else:
        l.append(0)
        print("Production {0} doesnt has left recursion".format(i + 1))
        if gam[k]!='#':
            op2 += gam[-1]
            for j in range(k+1,k+sizeofp[i]):
                op2 += gam[j]
            k = j+1
            op2 += gam[0]
op1 += "#"
if sum(l)==0:
    print("There is no left recursion")
else:
    print(op2)
    print(op1)