from pyecharts import ThemeRiver #导入Echarts绘图库
import pandas as pd #导入pandas用于读取excel数据

xlsfile = '河流图数据1.xlsx' #excel文件名
data=[] #备用空列表
df3=pd.read_excel(xlsfile) #读取excel数据
for eachone in range(len(df3.columns)-1): #循环读取每一列数据
    data.extend([[i,j,df3.columns[eachone+1]] \
                 for i,j in zip(range(len(df3.index)),\
                df3[df3.columns[eachone+1]])]) #将数据添加到data列表中

colors_list=['#FFA07A','#32CD32','#4169E1','#FAA460',\
             '#F0E68C','#8c564b','#e377c2','#7f7f7f','#bcbd22','#17becf']#备用颜色列表
range_color=[]#颜色数据空列表    
for i in range(len(df3.columns)-1):
    range_color.append(colors_list[i%10])#填充颜色
  
river = ThemeRiver()
river.add([df3.columns[i+1] for i in range(len(df3.columns)-1)], data, \
          is_label_show=False,label_color=range_color,\
          x_label=list(df3[df3.columns[0]]),x_name=df3.columns[0])#绘制主题河流图，传递自定义颜色列表
river.render()#在当前目录生成'render.html'文件，需手动用浏览器打开查看图片  

