import json
import open_initialize

def modify():
    dic={}
    #change_dic={}
    #val=[]
   # with open('test.txt')as f:
   #     lines=f.readlines()
   # for line in lines:
   #     line=line.strip('\n') #去掉换行符\n
   #    b=line.split(' ') #将每一行以空格为分隔符转换成列表
   #    dic[b[0]]=b[1]
    preference_dict=open_initialize.getpreference_type()
    preference_list=open_initialize.getpreference_poss()
    dic=zip(preference_dict,preference_list)
    print(dic)
   # with open('changetest.txt')as g:
   #    lines=g.readlines()
   # for line in lines:
   #    line=line.strip('\n') #去掉换行符\n
   #     b=line.split(' ') #将每一行以空格为分隔符转换成列表
   #    #change_dic.append(b)
   #    change_dic[b[0]]=b[1]
    temp_dict=open_initialize.gettemp_type()
    temp_list=open_initialize.gettemp_poss()
    #change_dic=zip(temp_dict,temp_list)
    for key in temp_dict:
        #print(key)
        if key in preference_dict:
            #print(key)
            temp1=preference_list[preference_dict[key]]
            temp2=temp_list[temp_dict[key]]
            temp=float(temp1)+float(temp2)*0.2#本次浏览中，更新的系数：*0.2（可以后期调参更改）
            if temp>=10 :#设置权值上限为10
                temp=10
            if temp<0 :#设置权值下限为0
                temp=0
            preference_list[preference_dict[key]]=temp
    #val=list(dic.value())
    with open('preference_poss.txt','w') as h:
        for line in range(len(preference_list)):
            h.write('%f\n'%(preference_list[line]))
#modify()
