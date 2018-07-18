from pyecharts import Graph
import pandas as pd #导入pandas，用于操作excel文件
import numpy as np
import matplotlib.pyplot as plt
import igraph   

df=pd.read_excel('阚老师数据1.xlsx')#打开excel文件
g=igraph.Graph(1)
g.add_vertices(df.index)
weights=[]
my_links=[] #备用空列表
for i in df.index:#外层循环，轮询excel每个列
    for j in df.columns:#内层循环，轮询excel每一行
        if df[j][i] >0:#大于0的值有效
            my_links.append({'source':i,'target':(j),'value':df[j][i]})
            g.add_edge(i,j)
            weights.append(df[j][i])
        else:
            pass

if not g.vs[0]['name']:
    g.delete_vertices(0)
result=g.community_multilevel(weights,True)

igraph.plot(result[1],mark_groups = True, margin = 20,
     vertex_label=[str(i) for i in range(len(df.index))])

#colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
colors_list=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral',
             'darkslateblue','#ADD8E6','#DDA0DD',
             '#FAA460','#F0E68C','#8c564b','#e377c2',
             '#7f7f7f','#bcbd22','#17becf']  
category_dic={}
for list_data in result[1]:
    for data in list_data:
        category_dic[df.index[data]]=df.index[list_data[0]]

sym_x=[]
sym_y=[]
sym=[]

for i in df.index:
    sym_x.append(sum(df.loc[i]))
    
for i in df.columns:
    sym_y.append(sum(df[i]))

for a,b in zip(sym_x,sym_y):
    sym.append(a+b)
      
        
my_nodes=[{'name':i,"symbolSize": int(np.sqrt(j)*np.sqrt(max(sym))/max(sym)*25),
           'category':category_dic[i],'value':j,'draggable':1} for i,j in zip(df.index,sym)]#生成节点数据框

category=[{'name':df.index[i[0]]} for i in result[1]]

        
graph = Graph("合作关系图",width=1000, height=900)
graph.add("", my_nodes, my_links, category,graph_gravity=1.0,
          is_legend_show=True,label_color=colors_list,
          is_label_show=True,label_pos="right",line_curve=0)
graph.render('graph.html')


