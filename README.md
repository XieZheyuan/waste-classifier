# waste-classifier
waste classifier program in Python 3(Chinese)

# 环境搭建
我们需要以下程序
- PyCharm Community Edition 2020.2（可选）
- Python 3


# 创建自己的数据集
新建一个目录`trains`,创建两个文件`train.csv`与`train.json`

```
trains/
    train.csv
    train.json
```

train.json留空,train.csv写入以下内容
```
塑料袋,1
塑料保鲜膜,1
一次性餐具,2
泥土,2
黄瓜,3
茄子,3
白菜,3
大豆,3
中药残渣,3
易拉罐,1
花朵,3
电池,4
影像带,4
荧光灯,4
```

>其中1代表**可回收垃圾**,2代表**干垃圾**(其他垃圾),3代表**湿垃圾**(厨余垃圾或易腐垃圾),4代表**有害垃圾**.

# 1、格式化数据程序
新建`formater.py`

```
trains/
    train.csv
    train.json
formater.py
```

## 安装jieba分词

```
pip install jieba -i https://pypi.douban.com/simple/
```

如果出现`Successfully installed jieba-***`字样，表示安装成功，否则可能是网络问题
> `https://pypi.douban.com/simple/`是豆瓣的镜像，如果使用默认镜像会超时

### 示例
```python
import jieba
s = "塑料保鲜膜"
print(list(jieba.cut(s, cut_all=True)))
```

结果：
```
Building prefix dict from the default dictionary ...
Loading model from cache C:\Users\mayn\AppData\Local\Temp\jieba.cache
Loading model cost 0.615 seconds.
Prefix dict has been built successfully.
['塑料', '保鲜', '保鲜膜']
```

`jieba.cut`用来分词，cut_all参数用来指定是否使用“全分词”模式。

[Jieba's Github](https://github.com/fxsjy/jieba)

## 开始正式编写
```python
import jieba
import json


def read(s: str):
    data = []
    for i in s.splitlines():
        k = []
        for j in i.split(","):
            k.append(j)
        data.append(k)
    return data


with open("trains/train.csv", "r", encoding="utf-8") as f:
    s = f.read()
print(s)
data = read(s)
print(data)
json_data = []
for i in data:
    print(i)
    field = i[0]
    field_jieba = list(jieba.cut(field, cut_all=True))
    json_data.append([field_jieba, int(i[1])])

with open("trains/train.json", "w") as f:
    s = json.dumps(json_data)
    f.write(s)

```

read函数：读取csv函数
for二重循环：解析csv，分词并写入数据
最后一个with语句：写入json

# 编写主程序
新建main.py
```python
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
except ZeroDivisionError:
    print("暂时没有收录哦！")

```
4-7行：读取训练集格式化后的json文件
14-21行：计算概率
22-30：输出结果

其实也没有用复杂算法，比较简单。

## 输出解释

### 收录情况

指该垃圾分词后的关键词占训练集总关键词的百分比。

## 类别的概率

指该垃圾分词后的关键词在训练集中指定的垃圾在某类型的百分比

## 示例输入输出
```
垃圾名称：
塑料
Building prefix dict from the default dictionary ...
Loading model from cache C:\Users\mayn\AppData\Local\Temp\jieba.cache
Loading model cost 0.622 seconds.
Prefix dict has been built successfully.
收录情况：12.5000%
可回收垃圾概率：100.0000%
干垃圾垃圾概率：0.0000%
湿垃圾垃圾概率：0.0000%
有害垃圾垃圾概率：0.0000%
程序结束
```
