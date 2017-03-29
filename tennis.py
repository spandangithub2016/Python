lst=[]
s=' '
while s !="a":
    s=input()
    lst.append(s)

lst.pop()
player_dic={}
for i in range(len(lst)):

    new_lst=[]
    p1=[]
    p2=[]
    p1c=p2c=0
    add1=add2=0
    temp=[]
    
    st=lst[i].split(":")
    new_lst.append(st[0])
    new_lst.append(st[1])
    st=st[2].split(",")
    
    for j in st:
        temp.append(j.split("-"))
    for k in temp:
        p1.append(k[0])
        p2.append(k[1])
    for i in range(len(p1)):
        add1=add1+int(p1[i])
        add2=add2+int(p2[i])
        if p1[i]>p2[i]:
            p1c=p1c+1
        else:
            p2c=p2c+1
    
    for i in range(len(new_lst)):
        c5=c3=0
        if len(p1)>3 and i==0:
            c5=c5+1
        elif i==0:
            c3=c3+1
        if new_lst[i] in player_dic and i==0:
            player_dic[new_lst[i]][0]=player_dic[new_lst[i]][0]+c5
            player_dic[new_lst[i]][1]=player_dic[new_lst[i]][1]+c3
            player_dic[new_lst[i]][2]=player_dic[new_lst[i]][2]+p1c
            player_dic[new_lst[i]][3]=player_dic[new_lst[i]][3]+add1
            player_dic[new_lst[i]][4]=player_dic[new_lst[i]][4]+p2c
            player_dic[new_lst[i]][5]=player_dic[new_lst[i]][5]+add2
        elif new_lst[i] in player_dic and i==1:
            player_dic[new_lst[i]][0]=player_dic[new_lst[i]][0]+c5
            player_dic[new_lst[i]][1]=player_dic[new_lst[i]][1]+c3
            player_dic[new_lst[i]][2]=player_dic[new_lst[i]][2]+p2c
            player_dic[new_lst[i]][3]=player_dic[new_lst[i]][3]+add2
            player_dic[new_lst[i]][4]=player_dic[new_lst[i]][4]+p1c
            player_dic[new_lst[i]][5]=player_dic[new_lst[i]][5]+add1
        elif i==0:
            player_dic[new_lst[0]]=[c5,c3,p1c,add1,p2c,add2]
        else:
            player_dic[new_lst[1]]=[c5,c3,p2c,add2,p1c,add1]

s_lst=[]
for i in range(len(player_dic)):
    s_lst.append(['O']*2)
i=0
for item in player_dic:
    s_lst[i][0]=item
    s_lst[i][1]=player_dic[item]
    i=i+1

for i in range(len(s_lst)):
    j=i+1
    while j<len(s_lst):
        if s_lst[i][1]<s_lst[j][1]:
            temp=s_lst[i]
            s_lst[i]=s_lst[j]
            s_lst[j]=temp
        j=j+1

for i in s_lst:
    print(i[0],i[1][0],i[1][1],i[1][2],i[1][3],i[1][4],i[1][5])
