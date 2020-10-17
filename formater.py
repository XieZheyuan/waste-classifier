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
