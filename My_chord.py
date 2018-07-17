import pandas as pd #导入pandas，用于操作excel文件
from bokeh.charts import output_file, Chord #导入bokeh扩展包，用于绘制弦图
from bokeh.io import show #导入文件操作中的显示网页函数

df=pd.read_excel('Chord.xlsx')#打开excel文件
my_links=[] #备用空列表
for i in range(len(df.columns)):#外层循环，轮询excel每个列
   # print(df[df.columns[i]])
    for j in range(len(df.index)):#内层循环，轮询excel每一行
        my_links.append({'target':(i+len(df.index)),'source':j,'value':df[df.columns[i]][j]})#生成从源到目标的字典,target跳过ABC

index=list(df.index)#将excel行标签转化为列表
index.extend(df.columns)#合并列表，得到所有标签
my_nodes=pd.DataFrame([{'name':i} for i in index])#生成节点数据框

my_nodes_df = pd.DataFrame(my_nodes)#生成用于绘图的节点数据
my_links_df = pd.DataFrame(my_links)#生成用于绘图的节点间连接

my_source_data = my_links_df.merge(my_nodes_df, how='left',
                             left_on='source', right_index=True)#合并数据，顺序按从源到目标的顺序

my_source_data = my_source_data.merge(my_nodes_df, how='left',
                                left_on='target', right_index=True)#再次合并数据，顺序按从目标到源的顺序

chord_from_df = Chord(my_source_data, source="name_x", target="name_y", value="value")#绘制弦图
output_file('my_chord-diagram.html')#当前文件夹输出网页文件
show(chord_from_df)#显示图片


