import numpy as np #导入python的数值计算扩展包numpy，并重命名为np
import matplotlib.pyplot as plt #导入Python的绘图扩展包matplotlib，并重新命名为plt
import pandas as pd #导入python的数据处理扩展包pandas，并重命名为pd，该包用于读写excel文件
import matplotlib.patches as mpatches
#plt.style.use('ggplot')#打开或者关闭R语言风格绘图  
plt.rc('font',family='SimHei')

sheet1=pd.read_excel('散饼数据表.xlsx','工作表1')#从excel的工作表1中读出数据，sheet名称根据实际情况修改
x=[i+1 for i in range(len(sheet1.columns))]#获取数据表的列，作为x轴辅助绘图数据
y_index=[i for i in range(len(sheet1.index))]#获取纵轴有多少行
y = [[i for y_data in range(len(x))] for i in range(1,len(y_index)+1)]#生成y轴辅助数据

fig, ax = plt.subplots()#创建子图
colors = ['gold', 'lightcoral', 'lightskyblue','yellowgreen']#颜色列表
ax.set(aspect="equal", title='散饼图示例')#设置标题以及图形的对称，不然饼会椭圆

for index in range(len(y_index)):#对转置后的每一列进行循环
    for i,j,r in zip(x,y[index],sheet1.T[sheet1.index[index]]):#循环执行，每次从x,y[index]中读取一个数，从转置后的excel表格中读取一列中的一个数据
        sheet=pd.read_excel('散饼数据表.xlsx',str(sheet1.columns[i-1])+str(sheet1.index[index]))#从excel中的相应sheet中读取数据，根据excel中的工作表名修改
        if r/max(sheet1.max())/2 < 0.2:
            ax.pie(sheet['数量'], explode=None, labels=None, colors='w',
      autopct='%d', shadow=False, startangle=90,radius=1/2,center=(i, j),frame=True,textprops={'fontsize':8})#绘制散饼图,
            ax.pie(sheet['数量'], explode=None, labels=None, colors=colors,
      autopct=None, shadow=False, startangle=90,radius=r/max(sheet1.max())/2,center=(i, j),frame=True)
        else:
            ax.pie(sheet['数量'], explode=None, labels=None, colors=colors,
      autopct='%d', shadow=False, startangle=90,radius=r/max(sheet1.max())/2,center=(i, j),frame=True,textprops={'fontsize':8})#绘制散饼图,面积大小由radius调节。
            
        #ax.pie([1], radius=np.sqrt(r/np.pi)/30/2,colors='w',center=(i, j),frame=True)#增加甜甜圈的圈,圈大小由radius调节
        #ax.text(i,j,str(r),fontsize=int(np.sqrt(r/np.pi)*0.8),
        #        horizontalalignment='center',verticalalignment='center')#增加数据标签,字体大小由fontsize调节
      
plt.grid(True)#增加栅格   
plt.xlabel('技术手段分类',size=14)#x轴说明
plt.ylabel('技术效果',size=14)#y轴说明
plt.title('XXX领域技术功效分析',size=14)#图片名称
plt.xticks(x,sheet1.columns)#利用excel表中的表格横轴更新x轴标度
plt.yticks([i+1 for i in range(len(sheet1.index))],list(sheet1.index))#利用excel表中的表格纵轴更新y轴标度
plt.xlim(0,len(sheet1.columns)+1)#设置x轴范围，美化图表
plt.ylim(0,len(sheet1.index)+1)#设置y轴范围，美化图表
plt.legend(handles=[mpatches.Patch(color=colors[i], label=(sheet.index[i])) for i in range(len(sheet.index))]
           ,loc='best',bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)
plt.show()#显示图片







