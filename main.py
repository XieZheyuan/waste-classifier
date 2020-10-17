import json
import jieba

with open("trains/train.json") as f:
    s = f.read()
s = json.loads(s)

name = input("垃圾名称：\n")
name_jieba = list(jieba.cut(name, cut_all=True))
# 计算样本比例
w=0
w1=0
wd = [0,0,0,0]
for i in s:
    for j in name_jieba:
        w+=1
        if j in i[0]:
            w1+=1
            wd[i[1]-1] += 1

wb = w1/w
try:
    print("收录情况：%.4f%%" % (wb * 100))
    print("可回收垃圾概率：%.4f%%" % ((wd[0] / w1) * 100))
    print("干垃圾垃圾概率：%.4f%%" % ((wd[1] / w1) * 100))
    print("湿垃圾垃圾概率：%.4f%%" % ((wd[2] / w1) * 100))
    print("有害垃圾垃圾概率：%.4f%%" % ((wd[3] / w1) * 100))
finally:
    print("程序结束")
