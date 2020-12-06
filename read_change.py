import json
def modify(tag,flag):
    dic={}
    change_dic={}
    with open('test.txt')as f:
        lines=f.readlines()
    for line in lines:
        line=line.strip('\n') #去掉换行符\n
        b=line.split(' ') #将每一行以空格为分隔符转换成列表
        dic[b[0]]=b[1]
    print(dic)
    with open('changetest.txt')as g:
        lines=g.readlines()
    for line in lines:
        line=line.strip('\n') #去掉换行符\n
        b=line.split(' ') #将每一行以空格为分隔符转换成列表
        #change_dic.append(b)
        change_dic[b[0]]=b[1]
    for key in change_dic.keys():
        print(key)
        if key in dic:
            print(key)
            temp1=dic[key]
            temp2=change_dic[key]
            temp=float(temp1)+float(temp2)
            dic[key]=str(temp)
            print(dic)
    json.dump(dic,open('test.txt','w'))
modify('happy',1)
