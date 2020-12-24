zcnum = 900

data=[0 for i in range(zcnum)]
roundNum = 8
layer = 0
step = 1
for j in range(zcnum):
    if j:
        if not roundNum == 0:
            data[j] = data[j-1]+step
            roundNum = roundNum - 1
        else:
            if not data[j-1] == 900 - 9*layer:
                data[j] = data[j-1]+180
                step = -step
            else:
                layer = layer + 1
                data[j] = 172 - 9*layer
                step = 1
            roundNum = 8
    else:
        data[j] = 172
    