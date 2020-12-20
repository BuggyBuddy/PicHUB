#行为推荐算法
import open_initialize
def get_max_dict():
    preference_dict=open_initialize.getpreference_type_list()
    preference_poss=open_initialize.getpreference_poss()
    max_poss=[0,0,0,0,0]
    max_dict=['','','','','']
    for i in range(len(preference_poss)):
        if preference_poss[i]>min(max_poss):
            #print(i)
            c=max_poss.index(min(max_poss))
            #print(c)
            max_poss[c]=preference_poss[i]
            max_dict[c]=preference_dict[i]
            sum_poss=sum(max_poss)
            for i in range(1,5):
                max_poss[i]=max_poss[i]/sum_poss
    return max_poss,max_dict

#max_poss,max_dict=get_max_dict()