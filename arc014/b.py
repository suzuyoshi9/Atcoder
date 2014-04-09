N = input()
R = []
flag = 0
for i in range(int(N)):
    W = raw_input()
    R.append(W)
    if(i!=0):
        mae = R[i-1]
        ima = R[i]
        if (mae[(len(mae)-1):] != ima[:1]):
            if i%2==0:
                print("LOSE")
                flag = 1
                break
            else:
                print("WIN")
                flag = 1
                break
        for j in range(len(R)-1):
            if(R[j]==R[i]):
                if i%2==0:
                    print("LOSE")
                    flag = 1
                    break
                else:
                    print("WIN")
                    flag = 1
                    break
        if flag == 1:
            break
if flag == 0:
    print "DRAW"
