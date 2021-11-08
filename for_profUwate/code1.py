#%matplotlib inline
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

#スケールフリーネットワークの作成
Node=10 #ノード数
network = nx.barabasi_albert_graph(Node,2,1) #バラバシアルバートモデル
nx.draw_networkx(network) #グラフの描画

#最短経路探索（スタート:1-9、ゴール:ノード9)
for i in range(Node):
    print("start=",i,"goal=",9,"shortest path = ",nx.shortest_path(network, source=i, target=9))


#各ノードが経由地点に選ばれる回数（手動で作成）
select=np.array([[1,0,0,1,0,0,0,0,0,1],[1,0,0,2,0,0,0,0,0,1],[1,0,0,2,0,0,0,0,0,1],[1,0,0,2,0,0,0,0,0,1]])


print("各ノードが経由地点に選ばれる回数=",select) #例 route[0][0]=2:ノード0が経由地点に選ばれる回数は2回

N=10 #格納数
#各ノード格納数10のリストを作成
x0=[]
x1=[]
x2=[]
x3=[]
x4=[]
x5=[]
x6=[]
x7=[]
x8=[]
x9=[]



#初期状態：各ノードともパケットを持っていない
for i in range(N):
    xa=0
    x0.append(xa)
    x1.append(xa)
    x2.append(xa)
    x3.append(xa)
    x4.append(xa)
    x5.append(xa)
    x6.append(xa)
    x7.append(xa)
    x8.append(xa)
    x9.append(xa)

#パケットの生成と移動　スタート1,3,7(パケットを生成)、ゴール9
t=0
count=0
while count < 4:
    print("count=",count)
#     #パケットの生成（リストの左から順番にパケットをうめていく）
#     for K in range(1):#各countでパケットを1つ生成
#        if x0[K]==0:#もし、x0[K]=0ならば
#          x0[K]=1#x0[0]=1
#        elif x0[K]!=0:#もし、x0[K]=0ならば
#          while x0[K]==1: #x0[K]=1になるまで右にずらしていく
#             t=t+1
#             K=t
#          x0[K]=1 #x0[K]=1でなくなった時点でのx0[K]を1とする
#          t=0
#     print("x0生成=",x0)
    #パケットの移動　各countでノード0はパケットを1つ次のノードの送る
    if sum(x0)==0: #リスト内にパケットがない時
        a=select[count][0] #ノード0が経由地点に選ばれる回数(他のノードから送られ来たパケットの数)
    elif sum(x0)!=0: #リスト内にパケットがあるとき
        a=select[count][0]-1#ノード0が経由地点に選ばれる回数(他のノードから送られ来たパケットの数)-ノード0が送り出したパケットの数
    b=sum(x0)+a #移動後のノード0のパケット数
    for K in range(N): #x0リストをリセット
        x0[K]=0
    for i in range(b): #パケットの数だけリストの左からうめていく
        x0[i]=1
    print("x0移動=",x0)

#ノード1-9でも同様の操作を行う
    
    #ノード1
    for K in range(1):
       if x1[K]==0:
         x1[K]=1
       elif x1[K]!=0:
         while x1[K]==1:
            t=t+1
            K=t
         x1[K]=1
         t=0
    print("x1生成=",x1)
    if sum(x1)==0:
        a=select[count][1]
    elif sum(x1)!=0:
        a=select[count][1]-1
    b=sum(x1)+a
    for K in range(N):
        x1[K]=0
    for i in range(b):
        x1[i]=1
    print("x1移動=",x1)
    
    #ノード2
#     for K in range(1):
#        if x2[K]==0:
#          x2[K]=1
#        elif x2[K]!=0:
#          while x2[K]==1:
#             t=t+1
#             K=t
#          x2[K]=1
#          t=0
#     print("x2生成=",x2)
    if sum(x2)==0:
        a=select[count][2]
    elif sum(x2)!=0:
        a=select[count][2]-1
    b=sum(x2)+a
    for K in range(N):
        x2[K]=0
    for i in range(b):
        x2[i]=1
    print("x2移動=",x2) 
    
    #ノード3
    for K in range(1):
       if x3[K]==0:
         x3[K]=1
       elif x3[K]!=0:
         while x3[K]==1:
            t=t+1
            K=t
         x3[K]=1
         t=0
    print("x3生成=",x3)
    if sum(x3)==0:
        a=select[count][3]
    elif sum(x3)!=0:
        a=select[count][3]-1
    b=sum(x3)+a
    for K in range(N):
        x3[K]=0
    for i in range(b):
        x3[i]=1
    print("x3移動=",x3)     

    #ノード4
#     for K in range(1):
#        if x4[K]==0:
#          x4[K]=1
#        elif x4[K]!=0:
#          while x4[K]==1:
#             t=t+1
#             K=t
#          x4[K]=1
#          t=0
#     print("x4生成=",x4)
    if sum(x4)==0:
        a=select[count][4]
    elif sum(x4)!=0:
        a=select[count][4]-1
    b=sum(x4)+a
    for K in range(N):
        x4[K]=0
    for i in range(b):
        x4[i]=1
    print("x4移動=",x4) 

    #ノード5
#     for K in range(1):
#        if x5[K]==0:
#          x5[K]=1
#        elif x5[K]!=0:
#          while x5[K]==1:
#             t=t+1
#             K=t
#          x5[K]=1
#          t=0
#     print("x5生成=",x5)
    if sum(x5)==0:
        a=select[count][5]
    elif sum(x5)!=0:
        a=select[count][5]-1
    b=sum(x5)+a
    for K in range(N):
        x5[K]=0
    for i in range(b):
        x5[i]=1
    print("x5移動=",x5)

    #ノード6
#     for K in range(1):
#        if x6[K]==0:
#          x6[K]=1
#        elif x6[K]!=0:
#          while x6[K]==1:
#             t=t+1
#             K=t
#          x6[K]=1
#          t=0
#     print("x6生成=",x6)
    if sum(x6)==0:
        a=select[count][6]
    elif sum(x6)!=0:
        a=select[count][6]-1
    b=sum(x6)+a
    for K in range(N):
        x6[K]=0
    for i in range(b):
        x6[i]=1
    print("x6移動=",x6)

    #ノード7
    for K in range(1):
       if x7[K]==0:
         x7[K]=1
       elif x7[K]!=0:
         while x7[K]==1:
            t=t+1
            K=t
         x7[K]=1
         t=0
    print("x7生成=",x7)
    if sum(x7)==0:
        a=select[count][7]
    elif sum(x7)!=0:
        a=select[count][7]-1
    b=sum(x7)+a
    for K in range(N):
        x7[K]=0
    for i in range(b):
        x7[i]=1
    print("x7移動=",x7)

    #ノード8
#     for K in range(1):
#        if x8[K]==0:
#          x8[K]=1
#        elif x8[K]!=0:
#          while x8[K]==1:
#             t=t+1
#             K=t
#          x8[K]=1
#          t=0
#     print("x8生成=",x8)
    if sum(x8)==0:
        a=select[count][8]
    elif sum(x8)!=0:
        a=select[count][8]-1
    b=sum(x8)+a
    for K in range(N):
        x8[K]=0
    for i in range(b):
        x8[i]=1
    print("x8移動=",x8)

    #ノード9
#     for K in range(1):
#        if x9[K]==0:
#          x9[K]=1
#        elif x9[K]!=0:
#          while x9[K]==1:
#             t=t+1
#             K=t
#          x9[K]=1
#          t=0
#     print("x9生成=",x9)
    if sum(x9)==0:
        a=select[count][9]
    elif sum(x9)!=0:
        a=select[count][9]
    b=sum(x9)+a
    for K in range(N):
        x9[K]=0
    for i in range(b):
        x9[i]=1
    print("x9移動=",x9)
    count=count+1